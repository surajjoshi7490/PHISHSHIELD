import ipaddress
import re
import socket
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class FeatureExtraction:
    def __init__(self, url):
        self.url = url
        self.features = []

        # Parse URL
        parsed = urlparse(url)
        self.domain = parsed.netloc
        self.scheme = parsed.scheme

        # Fetch page
        self.response = None
        self.soup = None
        try:
            self.response = requests.get(
                url,
                timeout=5,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            self.soup = BeautifulSoup(self.response.text, "html.parser")
        except:
            pass

        # Feature extraction
        self.features.extend([
            self.using_ip(),
            self.long_url(),
            self.short_url(),
            self.symbol_at(),
            self.redirecting(),
            self.prefix_suffix(),
            self.subdomains(),
            self.https_scheme(),
            self.favicon(),
            self.non_std_port(),
            self.https_in_domain(),
            self.request_url(),
            self.anchor_url(),
            self.links_in_scripts(),
            self.server_form_handler(),
            self.info_email(),
            self.abnormal_url(),
            self.website_forwarding(),
            self.status_bar_customization(),
            self.disable_right_click(),
            self.popup_window(),
            self.iframe_redirection(),
            self.links_pointing_to_page(),
            self.stats_report()
        ])

        # Force feature vector to length 30
        while len(self.features) < 30:
            self.features.append(0)

    # 1
    def using_ip(self):
        try:
            ipaddress.ip_address(self.domain)
            return -1
        except:
            return 1

    # 2
    def long_url(self):
        length = len(self.url)
        if length < 54:
            return 1
        elif length <= 75:
            return 0
        return -1

    # 3
    def short_url(self):
        pattern = r"bit\.ly|goo\.gl|tinyurl|t\.co|ow\.ly"
        return -1 if re.search(pattern, self.url) else 1

    # 4
    def symbol_at(self):
        return -1 if "@" in self.url else 1

    # 5
    def redirecting(self):
        return -1 if self.url.count("//") > 1 else 1

    # 6
    def prefix_suffix(self):
        return -1 if "-" in self.domain else 1

    # 7
    def subdomains(self):
        dots = self.domain.count(".")
        if dots == 1:
            return 1
        elif dots == 2:
            return 0
        return -1

    # 8
    def https_scheme(self):
        return 1 if self.scheme == "https" else -1

    # 9
    def favicon(self):
        if not self.soup:
            return -1
        for link in self.soup.find_all("link", href=True):
            if self.domain in link["href"]:
                return 1
        return -1

    # 10
    def non_std_port(self):
        return -1 if ":" in self.domain else 1


   # 11
    def https_in_domain(self):
        return -1 if "https" in self.domain else 1

    # 12
    def request_url(self):
        if not self.soup:
            return 0
        total, safe = 0, 0
        for tag in self.soup.find_all(["img", "audio", "embed", "iframe"], src=True):
            total += 1
            if self.domain in tag["src"]:
                safe += 1
        if total == 0:
            return 0
        ratio = safe / total
        return 1 if ratio > 0.8 else 0 if ratio > 0.5 else -1

    # 13
    def anchor_url(self):
        if not self.soup:
            return 0
        total, unsafe = 0, 0
        for a in self.soup.find_all("a", href=True):
            total += 1
            if (
                "#" in a["href"]
                or "javascript" in a["href"].lower()
                or "mailto" in a["href"].lower()
                or self.domain not in a["href"]
            ):
                unsafe += 1
        if total == 0:
            return 0
        ratio = unsafe / total
        return 1 if ratio < 0.3 else 0 if ratio < 0.6 else -1

    # 14
    def links_in_scripts(self):
        if not self.soup:
            return 0
        total, safe = 0, 0
        for tag in self.soup.find_all(["link", "script"], src=True):
            total += 1
            if self.domain in tag.get("src", ""):
                safe += 1
        if total == 0:
            return 0
        ratio = safe / total
        return 1 if ratio > 0.8 else 0 if ratio > 0.5 else -1

    # 15
    def server_form_handler(self):
        if not self.soup:
            return 0
        forms = self.soup.find_all("form", action=True)
        if not forms:
            return 1
        for form in forms:
            action = form["action"]
            if action in ["", "about:blank"]:
                return -1
            if self.domain not in action:
                return 0
        return 1

    # 16
    def info_email(self):
        if not self.response:
            return 1
        return -1 if re.search(r"mailto:", self.response.text) else 1

    # 17
    def abnormal_url(self):
        return 1 if self.domain in self.url else -1

    # 18
    def website_forwarding(self):
        if not self.response:
            return 0
        redirects = len(self.response.history)
        return 1 if redirects <= 1 else 0 if redirects <= 4 else -1

    # 19
    def status_bar_customization(self):
        return -1 if self.response and "onmouseover" in self.response.text else 1

    # 20
    def disable_right_click(self):
        return -1 if self.response and "event.button" in self.response.text else 1

    # 21
    def popup_window(self):
        return -1 if self.response and "alert(" in self.response.text else 1

    # 22
    def iframe_redirection(self):
        return -1 if self.response and "<iframe" in self.response.text.lower() else 1

    # 23
    def links_pointing_to_page(self):
        if not self.response:
            return 0
        count = len(re.findall(r"<a ", self.response.text))
        return 1 if count == 0 else 0 if count <= 2 else -1

    # 24
    def stats_report(self):
        try:
            ip = socket.gethostbyname(self.domain)
            blacklisted_ips = ["146.112.61.108", "121.50.168.88"]
            return -1 if ip in blacklisted_ips else 1
        except:
            return 1

    def getFeaturesList(self):
        return self.features