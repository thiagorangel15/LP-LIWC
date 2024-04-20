#!/usr/bin/env node
const liwc = require('./liwc.js');
const fs = require('fs')

// let a = liwc.fromText("my english is horrible");

fs.readFile("./arquivoIngles.txt","utf-8", (err, data) => {
    if (err){
        throw err
    }
    const palavras = data.split(/\s+/)
    const palavraTratadas = palavras.map(palavra => palavra.toLowerCase().replace(/[^\w\s]/gi,''))

    const contarSensacoes = (palavras, indice, contagem) => {
        if(indice >= palavras.length){
            return contagem
        }
        const palavra = palavras[indice]
        const respostaLIWC = liwc.fromText(palavra)

        contagem.swear += respostaLIWC.swear || 0
        contagem.anx += respostaLIWC.anx || 0
        contagem.posemo += respostaLIWC.posemo || 0
        contagem.negemo += respostaLIWC.negemo || 0

        return contarSensacoes(palavras, indice + 1, contagem)
    }


    const contagemInicial = {
        swear: 0,
        anx: 0,
        posemo: 0,
        negemo: 0
    }

    const contagemFinal = contarSensacoes(palavraTratadas,0,contagemInicial)
    const tamanhoTexto = palavraTratadas.length

   // console.log(contagemFinal)
   // console.log(tamanhoTexto)

    const percentualPosemo = (contagemFinal.posemo/tamanhoTexto)*100
    const percentualNegemo = (contagemFinal.negemo/tamanhoTexto)*100

    if(percentualPosemo > percentualNegemo){
        console.log(`${tamanhoTexto} palavras. ${contagemFinal.swear} Palavras ofensivas, ${contagemFinal.anx} Palavras de ansiedade. tom geral positivo: ${Math.round(percentualPosemo)}% versus ${Math.round(percentualNegemo)}% negativo;`)
    }
    else if (percentualNegemo > percentualPosemo){
        console.log(`${tamanhoTexto} palavras. ${contagemFinal.swear} Palavras ofensivas, ${contagemFinal.anx} Palavras de ansiedade. tom geral negativo: ${Math.round(percentualNegemo)}% versus ${Math.round(percentualPosemo)}% negativo;`)
    }
    else{
        console.log(`${tamanhoTexto} palavras. ${contagemFinal.swear} Palavras ofensivas, ${contagemFinal.anx} Palavras de ansiedade. tom geral neutro: ${Math.round(percentualPosemo)}% versus ${Math.round(percentualNegemo)}% negativo;`)
    }
})
