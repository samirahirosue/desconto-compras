# 🛒 Sistema de desconto progressivo de compras 🛍

## 📌 Sobre o projeto

Este projeto consiste no desenvolvimento de um sistema de desconto progressivo de compras para uma loja online.

O programa solicita ao usuário o valor total da compra, identifica a faixa de desconto correspondente e calcula o valor final da compra após a aplicação do desconto.

Neste projeto, foram utilizadas as estruturas condicionais if, elif e else da linguagem Python.

## 💰 Regras de desconto

O desconto aplicado é definido de acordo com o valor total da compra:

- Compras abaixo de R$ 200,00 → 5% de desconto
- Compras de R$ 200,00 até abaixo de R$ 300,00 → 10% de desconto
- Compras de R$ 300,00 ou mais → 15% de desconto

## 🧮 Lógica de cálculo

O programa utiliza as seguintes condições para determinar o desconto:


if valor_total < 200: #desconto de 5% para compras abaixo de R$ 200,00 
    
    print("O desconto nesta compra é de 5%") 
    
    desconto = valor_total * 0.05 
    
    valor_desconto = valor_total - desconto 


elif valor_total < 300: #desconto de 10% para compras entre R$ 200,00 até abaixo de R$ 300,00 
  
    print("O desconto nesta compra é de 10%") 
   
    desconto = valor_total * 0.10 
   
    valor_desconto = valor_total - desconto 


else: #desconto de 15% para compras de R$ 300,00 ou mais 
  
    print("O desconto nesta compra é de 15%") 
   
    desconto = valor_total * 0.15 
    
    valor_desconto = valor_total - desconto 

## 💻 Exemplo de execução

Bem-vindo ao sistema de desconto progressivo!

Informe o valor total da compra: 250
O desconto nesta compra é de 10%
O valor da compra com desconto é de R$ 225.00

## 🛠 Tecnologias utilizadas

![Python](https://img.shields.io/badge/python-blue?style=flat&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/git-orange?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-black?style=flat&logo=github&logoColor=white)
