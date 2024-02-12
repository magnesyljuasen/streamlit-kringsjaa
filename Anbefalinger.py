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
st.title("Energiplan Kringsjå")
st.header("Innledning")
with st.sidebar:
    st.image('src/img/sio-av.png', use_column_width="auto")

st.write("""Asplan Viak har på oppdrag for SiO utarbeidet en mulighetsstudie 
         for energiforsyning til Kringsjå studentby. Formålet med studien er å 
         få et overordnet beslutningsgrunnlag for strategisk valg av bærekraftig energiforsyning i et 30 års perspektiv.""")
with st.expander("Oppsummering"):
    st.write("""- • Den webbasert energianalysen utviklet i prosjektet er et dialogverktøy. Analysen er fleksibel, detaljert (timenivå), oversiktlig, lett å forstå og bør oppdateres jevnlig og utvikles videre. For eksempel kan energileveranse, fornybar energi, driftskostnader og verdi av egenprodusert energi inkluderes. """)
    st.write("""- • Resultatene fra de 5 scenarioene for framtidas energiforsyning viser at grunnvarme og solceller til alle byggene vil redusere behovet for kjøpt strøm fra strømnettet betydelig, både topplast (makseffekt) og over året.""")
st.subheader("Anbefalinger")
with st.expander("Nye varmepumper i varmesentral 1 (OMT72)"):
    st.write(""" Det trengs minst en ny varmepumpe, 
             helst to i varmesentral 1 i OMT72.  
             Det bør være en ny varmepumpe til varmt tappevann (for eksempel CO₂) 
             og en til romoppvarming. Varmepumpen som er i 
             varmesentral 1 trenger å skiftes ut. 
             """)
with st.expander("Varmegjenvinning fra gråvann"):
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
with st.expander("Tilrettelegging og lading av energibrønner i byggetrinn 3"):
    st.write(""" 
             Teknisk rom i byggetrinn 3 bør tilrettelegges 
             for lading av brønner. Konkret innebærer 
             dette å forberede med stusser på tur/retur på brønnkretsen.  
             Det kan også være aktuelt å forberede for lading av brønner 
             med varmepumpe for eksempel dersom det er overskudd på solstrøm 
             og negative strømpriser. Dette forutsetter at det installeres 
             en kurs med varmevekslere mellom varm og kald siden på varmepumpen.  
             """)
with st.expander("Lading og energiutveksling mellom brønnparkene - GeoTermos"):
    st.write(""" Det bør vurderes om det er hensiktsmessig å på sikt koble brønnparkene 
             innenfor området sammen med varmevekslere. Hensikten er at alle varmesentralene 
             kan utveksle energi med alle brønnparkene. Videre vil mer lading av energibrønnene 
             i sommerhalvåret gjøre det mulig å hente ut tilsvarende mer energi og effekt om vinteren. 
             En annen viktig motivasjon for mer lading av brønnene er vi per i dag ikke har oversikt 
             over hvor mye varme som hentes ut og tilbakeføres til brønnparkene. Uten denne 
             oversikten og med stadig mer effektive varmepumper som henter mer varme fra energibrønnene, 
             er det en risiko for at temperaturen i brønnparken på sikt synker og blir for lav. 
             Aktuelle kilder for lading er hybrid solceller og solfangere (PVT – se avsnitt 4.6), eventuelt tørrkjøler. 
             Ladingen kan være passiv eller aktiv med varmepumpe. """)
    st.write(""" På sikt kan energibrønnene lades så mye at temperaturen i brønnene når 20-25°C på sensommeren. 
             Det betyr at varmepumpene får et mye lavere temperaturløft og trenger mindre strøm (høyere COP). 
             Brønnparkene på Kringsjå utgjør et stort volum. Dersom temperaturen i dette 
             bergvolumet øker fra sitt naturlige nivå på ca. 8°C til 20-25°C er det betydelige mengder 
             varme som kan hentes ut. En slik løsning vil nesten være en GeoTermos 
             tilsvarende den som er etablert på Fjell skole i Drammen. Forskjellen er at 
             GeoTermosen i Drammen leverer varmen direkte fra energibrønnene til byggene 
             store deler av vinteren. Der når temperaturen i bergvolumet opp mot 40-45 °C etter 
             ladesesongen fordi brønnene står tett sammen. Brønnparkene på Kringsjå vil ikke nå så 
             høye temperaturer fordi avstanden mellom brønnene er større. Det vil også være en 
             begrensning i hvor høy temperatur kollektorslangene tåler (trolig maksimalt 40 °C). 
             I en slik løsning må alle energibrønnene ha samme type kollektorvæske. Fordelen med å 
             koble sammen, og høyere temperatur i brønnparkene, er større energisikkerhet (redundans) 
             og høyere selvforsyningsgrad av energi og effekt. Det hindrer også at temperaturen i 
             energibrønnene synker for lavt. """)
    st.write(""" Videre anbefales det å etablere en GeoTermos som varmeforsyning til byggetrinn 4. 
             Energibrønnene i GeoTermosen kan plasseres under byggene, og bør 
             tilrettelegges for utveksling av energi med de andre brønnparkene 
             og varmesentralene. I forkant av etableringen må det gjøres forundersøkelser 
             som avklarer berggrunnens egnethet for magasinering av varme. De to termiske 
             responstestene utført i forbindelse med brønnparken til byggetrinn 3 viser 
             gode forhold for lagring av varme.  Effektiv varmeledningsevne er målt til 2,9 W/m*K og 
             uforstyrret temperatur er 8,3 og 8,4°C (Hartvigsen 2023) """)
with st.expander("Instrumentering for oversikt energiflyt og publisering av driftsdata"):
    st.write(""" Hensikten med instrumentering for oversikt 
             over energiflyten og publisering av driftsdata er todelt: """)
    st.write("- • Bidrar til kontroll og optimalisert drift av energianleggene")
    st.write("- • Skaper interesse blant studentene på campus.") 
    st.write(""" Driftsdata fra solcellene og varmeanlegget som bør publiseres 
             er produsert energi og effekt, hentet energi fra omgivelsene, 
             COP – andel strøm i forhold til levert varme, kjøpt energi 
             fra strømnettet osv. Dataene kan for eksempel vises på en monitor 
             sentralt på området. Vektlegging av god visualisering øker 
             forståelsen av energisystemet for både studentene og SiO. """)
    st.write(""" Arbeidet i mulighetsstudien har avdekket at det er 
             nødvendig å se nærmere på instrumentering og overvåking av 
             energiflyten til og fra energibrønnene, samt brønntemperaturene. 
             I det videre arbeidet vil det være nødvendig å finne ut om det 
             trengs mer instrumentering (f.eks. energimålere, flow-, temperatur- 
             og trykkmålere). Som nevnt i avsnitt 4.4 er det helt avgjørende å til 
             enhver tid ha kontroll på energiflyten og temperaturene i energibrønnene. """)
with st.expander("Hybridsolceller og solfangere (PVT) som alternativ for solceller (PV)"):
    st.write(""" Det er aktuelt med mer lading av energibrønnene på Kringsjå. 
             Dette er årsaken til at hybrid solceller og solfangere (PVT) 
             bør vurderes som et alternativ til solceller (PV). 
             Noen typer PVT er designet for lading av energibrønner 
             (for eksempel DualSun) og gir passiv lavtemperatur 
             lading av brønnene. Hensikten er å øke kapasiteten 
             til grunnvarmeanlegget. """)
with st.expander("Økt termisk akkumulering"):
    st.write(""" Termisk akkumulering med vanntank, eventuelt faseendringsmateriale (PCM) 
             er et tiltak som øker kapasiteten på varmepumpeanlegget. 
             Hensikten med dette er å redusere behovet for spisslast. 
             Det vil si at varmepumpeanlegget kan dekke en større del av energi- 
             og effektleveransen. Nettselskapene setter opp effekttariffen, 
             noe som gjør det mer lønnsomt å redusere behovet for spisslast. 
             Framtidas forventede knapphet på energi og makseffekt gjør at både 
             behovet for strøm fra strømnettet i topplasttimen (makseffekt) og 
             over året bør begrenses. Knappheten tilsier at særlig topplasttimene kan bli kostbare. """)
with st.expander("Vannbåren varme og oppgradering av bygningsmassen"):
    st.write(""" I forbindelse med oppgradering av bygningsmassen anbefaler 
             vi å konvertere fra panelovner til vannbåren varme. 
             Gulvvarme med mindre avstand mellom rørene (for eksempel 15 cm) 
             anbefales siden varmen da kan distribueres med lavere temperatur. 
             Eventuelle vannbårne høytemperaturanlegg bør også konverteres 
             til lavtemperatur. Lave temperaturløft for varmepumpen gir høy ytelse (høy COP). """)
    st.write(""" Generelt oppfordres det til å gjøre en systematisk oppgradering av 
             bygningsmassen slik at den trenger mindre makseffekt og energi 
             over året (klimaskall, ventilasjon, vinduer, etterisolering mm.). """)
with st.expander("Inkludere kostnader og måledata i energianalysen"):
    st.write(""" Vi anbefaler å bygge videre på energianalyse-verktøyet som er utviklet for Kringsjå studentby. Dette kan være:""")
    st.write("- • Vise egenprodusert energi (solstrøm og varme fra energibrønner). ")
    st.write("- • Løpende verdiberegning av egenprodusert energi ut fra spotpris på strøm.")
    st.write("- • Inkludere investeringskostnader for ulike energitiltak og beregne lønnsomhet.")
    st.write("- • Oppdatere bygnings- og anleggsinfo etter hvert som tiltakene gjøres, som en digital tvilling.")

st.write("")
st.write("")
download_pdf()

if st.button("Gå til kartapplikasjon"):
    switch_page("Kartapplikasjon")