import streamlit as st

from pages import DecilePerformance, SegmentPerformance, CollectionEfficiency

st.title("FCE Model Monitoring")
st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
query_params = st.experimental_get_query_params()
#tabs = ["Segment Performance", "Decile Performance","Performance"]
tabs = ["SegmentPerformance", "DecilePerformance", "CollectionEfficiency"]
if "tab" in query_params:
    active_tab = query_params["tab"][0]
else:
    active_tab = "SegmentPerformance"

if active_tab not in tabs:
    st.experimental_set_query_params(tab="SegmentPerformance")
    active_tab = "SegmentPerformance"

li_items = "".join(
    f"""
    <li class="nav-item">
        <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
    </li>
    """
    for t in tabs
)
tabs_html = f"""
    <ul class="nav nav-tabs">
    {li_items}
    </ul>
"""

st.markdown(tabs_html, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
  
if active_tab == "DecilePerformance":
    DecilePerformance.write1()
elif active_tab == "SegmentPerformance":
    SegmentPerformance.write()
    #Performance.write1()
elif active_tab == "CollectionEfficiency":
    CollectionEfficiency.write()
    #Performance.write1()
else:
    st.error("Something has gone terribly wrong.")