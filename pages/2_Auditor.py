import openai

openai.api_key = "SUA_API_KEY_DA_OPENAI"

def auditor_mercado(nome_produto):
    # Prompt estruturado para forçar a IA a devolver em JSON limpo e respeitar os 5 países
    prompt = f"""
    Analise o produto de afiliados da gringa chamado '{nome_produto}'.
    Retorne uma resposta estritamente em formato JSON com a seguinte estrutura:
    {{
      "beneficios": ["beneficio 1", "beneficio 2"],
      "dores": ["dor 1", "dor 2"],
      "cpc_comparacao_5_paises": {{
         "USA": "$2.50", "UK": "$1.80", "Canada": "$2.10", "Australia": "$2.30", "Germany": "$1.40"
      }},
      "historico_12_meses_index_trends":,
      "veredicto_melhor_pais": "USA",
      "estrategia_recomendada": "Fundo de Funil no Google Ads utilizando bônus exclusivo na Pre-Sell."
    }}
    """
    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    
    return response.choices[0].message.content
