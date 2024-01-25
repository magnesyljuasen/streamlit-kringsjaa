import streamlit as st
import pandas as pd
import numpy as np
import os
import folium
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from shapely.geometry import Point, Polygon
from folium.plugins import Fullscreen
import time
import base64
from PIL import Image
from streamlit_extras.switch_page_button import switch_page


def streamlit_settings(title, icon):
    st.set_page_config(page_title=title, page_icon=icon, layout="centered", initial_sidebar_state='collapsed')
    with open("src/styles/main.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    st.markdown(
        """<style>[data-testid="collapsedControl"] svg {height: 3rem;width: 3rem;}</style>""",
        unsafe_allow_html=True,
    )

def download_pdf():
    pdf_file_path = "Rapport.pdf"

    with open(pdf_file_path, "rb") as file:
        pdf_bytes = file.read()

    st.download_button(
        label="Last ned fullstendig rapport",
        data=pdf_bytes,
        help="Trykk på knappen for å laste ned rapport",
        file_name="Rapport.pdf",
        key="pdf-download",
    )


streamlit_settings(title="Energy Plan Zero, Kringsjå", icon="h")
st.warning("Under arbeid...")
st.title("Energiplan Kringsjå")
st.header("Innledning")
with st.sidebar:
    st.image('src/img/sio-av.png', use_column_width="auto")

st.write("""Asplan Viak har på oppdrag for SiO utarbeidet en mulighetsstudie for energiforsyning til Kringsjå studentby. Formålet med studien er å få et overordnet beslutningsgrunnlag for strategisk valg av bærekraftig energiforsyning i et 30 års perspektiv.""")

st.header("Våre anbefalinger")
with st.expander("Tilrettelegging for varmegjenvinning fra gråvann"):
    st.write(
    """ 
    Det anbefales å etablere, evt. tilrettelegge for varmegjenvinning fra gråvann. 
    Mesteparten av energien til oppvarming av studentbyen er relatert til tappevann, 
    og gjenvinning av varme, både direkte til forvarming av tappevann og 
    indirekte via brønnkretsen er fordelaktig siden det reduserer tilført effekt 
    fra varmepumpen samt avlaster grunnvarmeanlegget akkurat når det trengs.  
    """)
    st.write(
    """
    Tilsvarende varmegjenvinning er allerede etablert ved SIT sine 
    grunnvarmeanlegg i Trondheim, (Moholt 50/50 og Moholt Alle), 
    og planlegges til studentboligene ved Nardoveien 12-14.  
    """)
    st.write(
    """
    Det er en fordel om gråvannet samles slik at gjenvinningen kan 
    etableres i et punkt, f.eks. et samlerør i bakken eller i byggene. 
    Her er det også aktuelt å vurdere pumpehuset. 
    """)
    st.write(
    """
    Estimert investering for å etablere gjenvinning av gråvann er ca.  1,5 – 2,5 MNOK.  
    """    
    )
with st.expander("Tilrettelegg for lading av brønner"):
    st.write(
    """
    Tilrettelegg i teknisk rom for lading av brønner, dvs. forberede med stusser 
    på tur/retur på brønnkretsen.  Det kan også være aktuelt å forberede for 
    lading av brønner med varmepumpe, f.eks. dersom det er et overskudd på solstrøm 
    og negative strømpriser. Dette forutsetter at det installeres en kurs med 
    varmevekslere mellom varm og kald siden på varmepumpen.  
    """
    )
with st.expander("Vurdere PVT – hybrid solceller og solfangere til både strømproduksjon og lading av brønnkrets istedenfor kun solceller (PV)"):
    st.write(
    """
    Se f.eks. Dualsun, hybrid PVT for lading av brønner.
    Dette kan være et alternativ til solceller og gir passiv lavtemperatur lading av brønnene.
    Hensikten med dette er å øke kapasiteten til grunnvarmeanlegget.  
    """
    )
with st.expander("Tilrettelegg for energiutveksling mellom brønnparkene innenfor Kringsjå."):
    st.write(
    """
    Det bør vurderes om det er hensiktsmessig å på sikt koble brønnparkene innenfor området sammen med varmevekslere.  
    """    
    )
with st.expander("Instrumentering og tilgjengeliggjøre driftsdata"):
    st.write(
    """
    Tilrettelegg for publisering av driftsdata fra varmeanlegget 
    (levert energi, effekt, hentet energi fra omgivelsene, COP, kjøpt energi fra strømnettet). 
    Visualisering av driftsdata fra anlegget for å skape interesse blant studenter 
    på campus. F.eks via monitor på sentral plass. 
    """
    )
with st.expander("Økt termisk akkumulering"):
    st.write(
    """
    Termisk akkumulering med vanntank (eventuelt faseendringsmateriale) for økt 
    kapasitet på varmepumpeanlegget, hensikten med dette er å redusere behovet for spisslast.  
    Dvs. varmepumpeanlegget kan dekken en større del av energi og effektleveransen. 
    Nettselskapene setter opp effekttariffen, noe som gjør det mer lønnsomt og 
    aktuelt å redusere behovet for spisslast.  
    """
    )
with st.expander("Omlegging til vannbåren varme for bygg med panelovn"):
    st.write(
    """
    
    """
    )
with st.expander("Oppgradering av klimaskall"):
    st.write(
    """
    
    """
    )
with st.expander("Tilrettelegging for varmegjenvinning fra avkastluft"):
    st.write(
    """ 
    """)
with st.expander("Ny varmepumpe i OMT72"):
    st.write(
    """
    - CO2 varmepumpe, bedre ytelsesfaktor
    - En varmepumpe til romoppvarming (lavtemperatur) og en til tappevann (høytemperatur).
    """)
with st.expander("Sesongvarmelager"):
    st.write(
    """
    
    """)



st.write("")
st.write("")
download_pdf()

if st.button("Gå til kartapplikasjon"):
    switch_page("Kartapplikasjon")







#st.header("Innledning")
#st.header("Dagens energi- og effektsituasjon")
#st.header("Tiltak")
#st.subheader("Utnyttelse av lokalt produsert elektrisitet")
#st.subheader("Fremtidig energibruk")
#st.subheader("Fjernvarme")
#st.subheader("Grunnvarme")
#st.subheader("Grunnvarme med sesonglagring")
#st.subheader("Gråvannsgjenvinning")
#st.subheader("Solvarme")
#st.subheader("Solceller")
#st.subheader("Lagring av strøm i batterier")
#st.subheader("Reduksjon av effekttopper med varmelagring, evt. større varmepumpe")
