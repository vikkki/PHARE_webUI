import streamlit as st

import streamlit_extras
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row


## Layout, main body


st.title("Welcome to PhAre")
st.text("(Ph)ysiology (A)ge P(re)diction")

st.text('''
Inferring age with blood transcriptome data 
''')

#st.markdown('<p class="big-font"> big-font test !!</p>', unsafe_allow_html=True)

col11, col12, col13 = st.columns([4,6,4])
with col12:
    st.image("static/treering.png", use_column_width=True)

st.markdown("<p style='text-align:center; color:LightGray;'>Like tree rings, time carves massage in our blood, but not always evenly</p>", unsafe_allow_html=True)


st.subheader("PhAre prediction tools")
st.markdown("To build a transcriptome-based physiological age predictor model, we compiled scRNA-seq datasets from PBMCs of healthy 117 individuals spanning one lifespan, which contained more than one million cells. All cells received cell annotation based on `Panage_data`, and then the proportion of all immune cell types was calculated to train the PHARE model.")

st.markdown("PHARE utilized two different pipelines for `scRNA-seq` and `bulk RNA-seq` data to predict physiological age from new datasets ")

st.image('static/phare_sch1.png')


st.subheader("PhAre database `Panage_data`")

st.markdown("Currently, we had 24 scRNA-seq datasets from healthy individuals across different age groups have been integrated, annotated and re-investigated, they are available for explore online.")
left_col, cent_col,right_col = st.columns([5, 5, 5])
with cent_col:
    st.image('static/age_group_illustration.jpg', caption='Age atlas group orgnization')




#st.subheader("Citation")
#st.text("<*/ bioRxiv link here /*>")

st.divider()
st.markdown('''<p>
Developed by:\n
Cangang Zhang, Tao Ren, Xiaofan Zhao
</p>
''', unsafe_allow_html = True)
st.markdown('''<p>
<a href="http://xiazlab.org/">XiaLab</a> @ OHSU
</p>''', unsafe_allow_html = True)


links_row = row(2, vertical_align="center")
links_row.link_button(
    "📖  Model source code",
    "https://github.com/cliffren/PHARE",
    use_container_width=True,
)
links_row.link_button(
    "🐙  Visit website repository",
    "#",
    use_container_width=True,
)