import streamlit as st
import pandas as pd
import plotly.express as px

#Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")



#para rodar o codigo, abra o terminal e digite: streamlit run codigo.py




#titulo Sistema
st.write("# Sistema de Vendas")

#Secção Cadastro de Vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

#logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada com sucesso!")







# secão de Visualizar vendas
st.write("## Vendas Cadastradas")

st.dataframe(tabela_vendas)






# Seção de Dashboard
st.write("## Dashboard")


#Card/Metricas -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento:,.2f}")


#Grafico de Barras/Coluna -> Venda por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1) #exibe o grafico na tela do streamlit

#Grafico de Pizza -> Venda por produto  
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)