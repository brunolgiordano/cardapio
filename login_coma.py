import streamlit as st
import mysql.connector
import pandas as pd
import warnings
st.header("Bem Vindo ao Rancho do Comanche", divider=True)
form = st.form("my_form")
form.title("App. Comanda Eletrônica")
st.session_state['nro_comanda'] = 0
nro_comanda =  form.text_input("Digite Nro da Comanda")
senha = form.text_input("Digite a Senha do seu Ticket", type  = "password")  
submitted = form.form_submit_button("Clique Aqui...")
if submitted:        
		try:
			warnings.filterwarnings("ignore")
			cnx = mysql.connector.connect(user='qsd', password='1234',host='127.0.0.1',database='20210829000001b')
			sql = "SELECT * FROM comanda_aux where comanda  = %s and codigo = %s"
			mycur = cnx.cursor(dictionary=True,buffered=True)
			valor = (nro_comanda, senha)
			mycur.execute(sql,valor)
			row = mycur.fetchone()
			if row :
				st.session_state['nro_comanda']  = row['comanda']
				st.switch_page("pages/comanda.py")
			else:
				form.write("Comanda ou Senha Incorretos")
			
		except mysql.connector.Error as err:
  			   form.write("Something went wrong: {}".format(err))

        
