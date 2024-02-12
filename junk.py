gamle_anefalinger = """
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



"""



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
