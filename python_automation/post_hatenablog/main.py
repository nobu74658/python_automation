# https://tomowarkar.github.io/blog/posts/hatena_api/

from datetime import datetime
import requests as req

HATENA_ID = "your hatena id"
BLOG_DOMAIN = "your blog domain"
API_KEY = "your api key"
BASE_URL = f"https://blog.hatena.ne.jp/{HATENA_ID}/{BLOG_DOMAIN}/atom"


def hatena_entry(title, content, categorys=[], updated="", draft=False):
    """はてなブログへの投稿
    Attributes:
      HATENA_ID, API_KEY, BASE_URL (str)

    Args:
      title (str):
      content (str):
      categorys (List[str]):
      updated (str): %Y-%m-%dT%H:%M:%S
      draft (bool):

    Returns:
      str: xml
    """
    updated = updated if updated else datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    draft = "yes" if draft else "no"
    def category(x): return "\n".join([f"<category term='{e}' />" for e in x])
    categorys = category(categorys) if category else ""

    xml = f"""<?xml version="1.0" encoding="utf-8"?><entry xmlns="http://www.w3.org/2005/Atom" xmlns:app="http://www.w3.org/2007/app">
      <title>{title}</title><author><name>name</name></author><content type="text/markdown">{content}</content>
      <updated>{updated}</updated>{categorys}<app:control><app:draft>{draft}</app:draft>
      </app:control></entry>""".encode(
        "UTF-8"
    )
    r = req.post(BASE_URL + "/entry", auth=(HATENA_ID, API_KEY), data=xml)
    return r.text


if __name__ == "__main__":
    import sys

    _, arg = sys.argv
    with open(arg, "r") as f:
        title, categorys, *content = f.readlines()
    categorys = categorys.split(",")
    content = "\n".join(content)
    r = hatena_entry(title, content, categorys)
    print(r)
