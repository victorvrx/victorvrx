# COMMMMM AIIIII
from seleniumbase import Driver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
from selenium.webdriver.chrome.options import Options
import numpy as np
from scipy.stats import poisson
import requests


driver = Driver(uc=True)

driver.get("https://www.bet365.com/?#/IP/B1")

driver_2 = Driver(uc=True)
driver_2.get("https://esoccerbet.com.br/plataforma/")
driver_2.maximize_window()

lista_unica=[]
lista_unica_2=[]
# Filter data
filtered_data = []
lista_mestre_2=[]
lista_mestre=[]
start_time = time.time()
combo_list=[]

token = '6579676569:AAHNRarJ3UxUoTVj3Ju4zODKhCv5sWuf0M8'
#chat_id = '6657360941'  chat_id do bot
chat_id = "-4159632536" # chat id do grupo

# mostra o id do último grupo adicionado
def last_chat_id(token):
    try:
        url = "https://api.telegram.org/bot{}/getUpdates".format(token)
        response = requests.get(url)
        if response.status_code == 200:
            json_msg = response.json()
            for json_result in reversed(json_msg['result']):
                message_keys = json_result['message'].keys()
                if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys):
                    return json_result['message']['chat']['id']
            print('Nenhum grupo encontrado')
        else:
            print('A resposta falhou, código de status: {}'.format(response.status_code))
    except Exception as e:
        print("Erro no getUpdates:", e)

# enviar mensagens utilizando o bot para um chat específico
def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)
        
        
        



def processar_sublista(sublista):
        # Extrair os nomes entre parênteses, converter para minúsculas e remover espaços
        nomes_entre_parenteses = [item.split('(')[1].split(')')[0].strip().lower() for item in sublista[1:3]]

        # Juntar os nomes entre parênteses e adicionar à lista na posição zero
        sublista.insert(0, ''.join(nomes_entre_parenteses))

        return sublista


def calculate_cumulative_probability_less_than(total_goals, lambda_teamA_goals_for, lambda_teamA_goals_against, lambda_teamB_goals_for, lambda_teamB_goals_against):
    prob_less_than = 0
    for i in range(int(total_goals)):
        for j in range(int(total_goals)):
            prob_less_than += poisson.pmf(i, lambda_teamA_goals_for) * poisson.pmf(int(total_goals) - i, lambda_teamB_goals_against) * \
                              poisson.pmf(j, lambda_teamB_goals_for) * poisson.pmf(int(total_goals) - j, lambda_teamA_goals_against)
    return prob_less_than

def calculate_cumulative_probability_more_than(total_goals, lambda_teamA_goals_for, lambda_teamA_goals_against, lambda_teamB_goals_for, lambda_teamB_goals_against):
    prob_more_than = 0
    for i in range(int(total_goals) + 1):
        for j in range(int(total_goals) + 1):
            prob_more_than += poisson.pmf(i, lambda_teamA_goals_for) * poisson.pmf(j, lambda_teamB_goals_for) * \
                              poisson.pmf(int(total_goals) - i, lambda_teamA_goals_against) * poisson.pmf(int(total_goals) - j, lambda_teamB_goals_against)
    
    # Adjusted to ensure the probability is at most 1
    return min(1, prob_more_than)

def evaluate_over_under(total_goals, lambda_teamA_goals_for, lambda_teamA_goals_against, lambda_teamB_goals_for, lambda_teamB_goals_against):
    probability_less_than = calculate_cumulative_probability_less_than(total_goals, lambda_teamA_goals_for, lambda_teamA_goals_against, lambda_teamB_goals_for, lambda_teamB_goals_against)
    probability_more_than = calculate_cumulative_probability_more_than(total_goals, lambda_teamA_goals_for, lambda_teamA_goals_against, lambda_teamB_goals_for, lambda_teamB_goals_against)
    
    return total_goals, probability_less_than, probability_more_than, "more_than" if probability_more_than > probability_less_than else "less_than"

def analyze_over_under(lambda_teamA_goals_for, lambda_teamA_goals_against, lambda_teamB_goals_for, lambda_teamB_goals_against, linha_gols):
    results = []

    for total_goals in np.arange(0.25, 9, 0.25):
        results.append(evaluate_over_under(total_goals, lambda_teamA_goals_for, lambda_teamA_goals_against, lambda_teamB_goals_for, lambda_teamB_goals_against))

    max_prob_value = max(max(result[1], result[2]) for result in results)

    # Filter rows with the same maximum result
    max_prob_rows = [result for result in results if max(result[1], result[2]) == max_prob_value]

    for row in max_prob_rows:
        if linha_gols == row[0]:
            return "nao entrar"#row[3]
    
    # If linha_gols is not in the list of max probability rows
    if linha_gols < max_prob_rows[0][0]:
        return "more_than"
    elif linha_gols > max_prob_rows[0][0]:
        return "less_than"

try:

    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.iip-IntroductoryPopup > div > div.iip-IntroductoryPopup_Cross")))
    element.click()
    
    
    element = WebDriverWait(driver, 4).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div:nth-child(1) > div > div.wc-WebConsoleModule_SiteContainer > div.wc-PageView > div > div > div > div > div > div > div > div.ovm-OverviewView_Content > div.ovm-OverviewView_Classification.ovm-OverviewView_Classification-1 > div.ovm-ClassificationHeader.ovm-ClassificationHeader-1 > div.ovm-ClassificationMarketSwitcher > div" )))
    element.click()

    sleep(1)
    element = WebDriverWait(driver, 4).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div:nth-child(1) > div > div.wc-WebConsoleModule_SiteContainer > div.wc-PageView > div > div > div > div > div > div > div > div.ovm-OverviewView_Content > div.ovm-OverviewView_Classification.ovm-OverviewView_Classification-1 > div.ovm-ClassificationHeader.ovm-ClassificationHeader-1 > div.ovm-ClassificationMarketSwitcher > div > div.ovm-ClassificationMarketSwitcherDropdownPopup > div.ovm-ClassificationMarketSwitcherDropdownPopup_Contents > div:nth-child(4)" )))
    element.click()
    
    


except Exception:
    pass

while True:
    
    

    try:
    
        elemento = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div > div.wc-WebConsoleModule_SiteContainer > div.wc-PageView > div > div > div > div.ip-InPlayModule_Container > div > div > div > div.ovm-OverviewView_Content > div.ovm-OverviewView_Classification.ovm-OverviewView_Classification-1"))
                )
        
    except Exception:
        
        # Close the current window
        driver.close()
        driver_2.close()

        # Quit the entire browser session
        driver.quit()
        driver_2.quit()
        
        driver = Driver(uc=True)
        
        driver.get("https://www.bet365.com/?#/IP/B1")
        
        # esoccer
        driver_2 = Driver(uc=True)
        driver_2.get("https://esoccerbet.com.br/plataforma/")
        driver_2.maximize_window()
        
        
        try:

            element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.iip-IntroductoryPopup > div > div.iip-IntroductoryPopup_Cross")))
            element.click()
            
            
            
            element = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div:nth-child(1) > div > div.wc-WebConsoleModule_SiteContainer > div.wc-PageView > div > div > div > div > div > div > div > div.ovm-OverviewView_Content > div.ovm-OverviewView_Classification.ovm-OverviewView_Classification-1 > div.ovm-ClassificationHeader.ovm-ClassificationHeader-1 > div.ovm-ClassificationMarketSwitcher > div" )))
            element.click()

            sleep(1)
            element = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div:nth-child(1) > div > div.wc-WebConsoleModule_SiteContainer > div.wc-PageView > div > div > div > div > div > div > div > div.ovm-OverviewView_Content > div.ovm-OverviewView_Classification.ovm-OverviewView_Classification-1 > div.ovm-ClassificationHeader.ovm-ClassificationHeader-1 > div.ovm-ClassificationMarketSwitcher > div > div.ovm-ClassificationMarketSwitcherDropdownPopup > div.ovm-ClassificationMarketSwitcherDropdownPopup_Contents > div:nth-child(4)" )))
            element.click()


        except Exception:
            pass
        
        
        elemento = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div > div.wc-WebConsoleModule_SiteContainer > div.wc-PageView > div > div > div > div.ip-InPlayModule_Container > div > div > div > div.ovm-OverviewView_Content > div.ovm-OverviewView_Classification.ovm-OverviewView_Classification-1"))
                )
    
    

    
            # Obtém o texto do elemento
    texto_elemento = elemento.text    

    lines = texto_elemento.split('\n')

    categories_to_keep = ["E-soccer - Battle - 8 minutos de jogo", "E-soccer Adriatic League - 10 minutos de jogo", "E-soccer - GT Leagues - 12 mins de jogo"]

    # Flag to indicate whether to keep data
    keep_data = False

    filtered_data=[]
    for item in lines:
        if item in categories_to_keep:
            keep_data = True
        if keep_data:
            filtered_data.append(item)
    
    filtered_data_2=[]
    
    filtered_data_2 = [item for item in filtered_data if item not in ['Mais De', 'Menos De']]
    filtered_data_2 = [item for item in filtered_data_2 if item not in ['GOL']]

    filtered_data_2

    data = filtered_data_2
    result = []
    current_game = []
    lista_game=[]

    for item in data:
        if 'jogo' in item:
            # Se a palavra 'jogo' estiver presente, começamos um novo jogo
            if current_game:
                result.append(current_game)
            current_game = [item]  # Iniciar uma nova sublista com o nome da liga
        else:
            current_game.append(item)  # Adicionar as informações do jogo à sublista

    # Adicionar a última sublista (último jogo)
    if current_game:
        result.append(current_game)

    # Imprimir o resultado
    for game in result:
        lista_game.append(game)



    #-----------------------------------
    dados = lista_game
    resultados=[]
    for sublista in dados:
    # Iterando sobre a lista a partir do segundo item
        for i in range(1, len(sublista)):
            # Verificando se os dois itens consecutivos contêm "Esports"
            if "Esports" in sublista[i] and "Esports" in sublista[i + 1]:
                # Verificando os oito itens consecutivos seguintes com menos de 8 strings cada
                if all(len(item) < 8 for item in sublista[i + 2:i + 10]):
                    # Se encontrarmos o padrão, você pode realizar as operações desejadas aqui
                    if len(sublista[i + 2:i + 10])==8:
                        #print(sublista[0])
                        #print("Padrão encontrado!")
                        #print("Item 1:", sublista[i])
                        #print("Item 2:", sublista[i + 1])
                        #print("Itens seguintes:", sublista[i + 2:i + 10])
                        resultado = [
                            sublista[0],
                            str(sublista[i]),
                            str(sublista[i + 1])
                        ]
                        resultado.extend(sublista[i + 2:i + 10])

                        resultados.append(resultado)


    # Agora 'resultados' conterá listas com as informações que você queria imprimir

    lista_mestre=[]
    # Exibindo as listas filtradas
    for i, sublista in enumerate(resultados):

        resultados_codigo = processar_sublista(sublista)

        if ',' in resultados_codigo[8]:
            # Split the seventh item into two numbers
            range_values = resultados_codigo[8].split(',')

            # Calculate the average of the two numbers
            average = (float(range_values[0]) + float(range_values[1])) / 2

            # Replace the original seventh item with the calculated average
            resultados_codigo[8] = str(average)
            resultados_codigo[10] = str(average)

            lista_mestre.append(resultados_codigo)

        else:
            lista_mestre.append(resultados_codigo)
            
            
            
            

    # Print the modified data
    for match in reversed(lista_mestre):

        
        codigo = match[0]


        if codigo not in lista_unica :
            
            
            
            #print(match)
            lista_mestre_2.append(match)
            lista_unica.append(codigo)
            
            
            i = 1  # Starting index
            
            #sleep(2)
            
            lista_mestre_esoccer = []
            while True:
                try:
                    element = WebDriverWait(driver_2,0.5).until(
                    EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[3]/div[3]/div[{i}]/div[1]/div[1]/div[1]/a[1]")))
                    home = element.text

                    element = WebDriverWait(driver_2,0.3).until(
                    EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[3]/div[3]/div[{i}]/div[1]/div[1]/div[3]/a[1]")))
                    away = element.text

                    codigo_esoccer = home + away

                    element = WebDriverWait(driver_2,0.01).until(
                    EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[3]/div[3]/div[{i}]/div[1]/div[2]/div[1]/div[3]/span")))
                    jogos_home = element.text

                    element = WebDriverWait(driver_2,0.01).until(
                    EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[3]/div[3]/div[{i}]/div[1]/div[2]/div[3]/div[3]/span")))
                    jogos_away = element.text

                    element = WebDriverWait(driver_2,0.01).until(
                    EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[3]/div[3]/div[{i}]/div[1]/div[2]/div[1]/div[2]/span[1]")))
                    media_feito_home = element.text

                    element = WebDriverWait(driver_2,0.01).until(
                    EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[3]/div[3]/div[{i}]/div[1]/div[2]/div[1]/div[2]/span[2]")))
                    media_sofrido_home = element.text

                    element = WebDriverWait(driver_2,0.01).until(
                    EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[3]/div[3]/div[{i}]/div[1]/div[2]/div[3]/div[2]/span[1]")))
                    media_feito_away = element.text

                    element = WebDriverWait(driver_2,0.01).until(
                    EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[3]/div[3]/div[{i}]/div[1]/div[2]/div[3]/div[2]/span[2]")))
                    media_sofrido_away = element.text



                    #print(codigo_esoccer,jogos_home,jogos_away,media_feito_home,media_sofrido_home,media_feito_away,media_sofrido_away)
                    lista_esoccer =[]
                    novos_itens = [codigo_esoccer, jogos_home, jogos_away, media_feito_home, media_sofrido_home, media_feito_away, media_sofrido_away]
                    lista_esoccer.extend(novos_itens)
                    #print(lista_esoccer)
                    if lista_esoccer not in lista_mestre_esoccer:
                        lista_mestre_esoccer.append(lista_esoccer)
                        
                    i += 1 

                    if (match[0] == lista_esoccer[0]) or (len(lista_mestre_esoccer)>20):
                        break

                except Exception:
                    # If NoSuchElementException is raised, the element is not found
                    #print(f"Element not found for index {i}")
                    i = 1  # Move to the next index and continue the loop
                    break
                    
            # Estatistica e envio para telegram entra aqui ------------------------------------------------------------       
            if match[0] == lista_esoccer[0]:
                
                tempo_atual = time.time()
                lista_unica_2= [item for item in lista_unica_2 if item[1] > tempo_atual]
                
                encontrado = any(match[0] in lista for lista in lista_unica_2)

                if encontrado:
                    
                    pass
                else:
                    tempo_atual = time.time()
                    tempo_de_expiracao = tempo_atual + ( 9 * 60)
                    if "00:" in match[4]:
                        match.append(tempo_de_expiracao)  # Use append em vez de extend
                        lista_unica_2.append([match[0], match[12]])
                        
                        
                        lambda_teamA_goals_for = float(lista_esoccer[3])
                        lambda_teamA_goals_against =  float(lista_esoccer[4])
                        lambda_teamB_goals_for =  float(lista_esoccer[5])
                        lambda_teamB_goals_against = float(lista_esoccer[6]) 
                        linha_gols = float(match[8]) 
                        
                        result_def = analyze_over_under(lambda_teamA_goals_for, lambda_teamA_goals_against, lambda_teamB_goals_for, lambda_teamB_goals_against, linha_gols)
                        
                        if result_def == "more_than":
                            print(match,"Over:",match[8])
                            print(lista_esoccer)
                            mensagem = "Over Asiático "+ match[8] + "@" +  match[9]  +"\n" +"\n" +  "⚽❄️ "  +  match[1] +"\n" +"\n"+ match[2] +"\n"+ " X " +"\n"+ match[3] +"\n" +"\n" + 'https://www.bet365.com/?#/IP/B1'

                            #URL = f"https://api.telegram.org/bot6579676569:AAHNRarJ3UxUoTVj3Ju4zODKhCv5sWuf0M8/sendMessage?chat_id=6657360941&text={mensagem}"
                            #resposta = requests.get(URL)
                            msg = mensagem
                            send_message(token, chat_id, msg)
                            
                            
                        elif result_def == "less_than":
                            print(match,"Under:",match[8])
                            print(lista_esoccer)
                            mensagem = "Under Asiático "+ match[8] + "@" +  match[11]  +"\n" +"\n" +  "⚽🔥 "  +  match[1] +"\n" +"\n"+ match[2] +"\n"+ " X " +"\n"+ match[3] +"\n" +"\n" + 'https://www.bet365.com/?#/IP/B1'
                            
                            #URL = f"https://api.telegram.org/bot6579676569:AAHNRarJ3UxUoTVj3Ju4zODKhCv5sWuf0M8/sendMessage?chat_id=6657360941&text={mensagem}"
                            #resposta = requests.get(URL)
                            msg = mensagem
                            send_message(token, chat_id, msg)
                            
                        else:
                            pass

                        #print(lista_unica_2)
                    else:
                        pass
    
            else:
                pass

            #print(lista_mestre_esoccer)


            
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= 900 :  # 12 minutes in seconds
            # After 12 minutes, clear lista_unica and update start_time
            lista_unica = []
            lista_mestre=[]
            #lista_unica_2=[]
            start_time = time.time()
        else:
            pass
