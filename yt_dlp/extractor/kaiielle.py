from .patreon import PatreonIE


class KaiielleIE(PatreonIE):
    IE_NAME = 'kaiielle'
    _VALID_URL = r'https?://(?:www\.)?kaiielle\.com/(?:creation\?hid=|(?:[^/?#]+/)?posts/(?:[\w-]+-)?)(?P<id>\d+)'
    _TESTS = []
