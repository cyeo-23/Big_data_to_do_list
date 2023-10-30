"""Utility functions for customizing Streamlit applications."""
import streamlit as st
from htbuilder import HtmlElement, div, hr, p, styles, img, a
from htbuilder.units import percent, px
from streamlit.components.v1 import html


def image(src_as_string, **style):
    """Return an image element with the specified source and styles."""
    return img(src=src_as_string, style=styles(**style))


def link(href, text, **style):
    """Return a link element with the specified href, text and styles."""
    return a(_href=href, _target="_blank", style=styles(**style))(text)


def nav_page(page_name, timeout_secs=3):
    """Navigate to a new page after the given number of seconds."""
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith(
                        "/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(
                        attempt_nav_page, 100, page_name,
                        start_time,
                        timeout_secs);
                } else {
                    alert(
                        "Unable to navigate to page '" + page_name +
                        "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


def layout(*args):
    """Create and display a layout with the given elements."""
    # Define styles for the page and footer
    page_style = """
    <style>
        # MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp { bottom: 105px; }
    </style>
    """
    footer_style = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="Green",
        text_align="center",
        height="auto",
        opacity=1
    )
    hr_style = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(style=footer_style)(
        hr(style=hr_style),
        body
    )

    st.markdown(page_style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, (str, HtmlElement)):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    """Display a custom footer on the Streamlit page."""
    elements = ["To do list App"]
    layout(*elements)
