from groq import Groq

def lama_response(prompt):
    print(f"Received prompt: {prompt}")
    client = Groq(
        api_key='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'
    )
    
    print("Groq client initialized.")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama3-70b-8192",
    )
    
    response = chat_completion.choices[0].message.content
    print(f"Response generated: {response}")
    return response

def process_string(input_string):
    input_string = input_string.replace('*', '')
    lines = input_string.split(':')
    processed_string = '\n'.join(lines)
    return processed_string


if __name__ == '__main__':
    test_prompt = "fă Logical fallacy detection Într-un interviu pentru Sputnik Moldova, Irina Vlah a spus că ea înțelege scopul acestui referendum - Maia Sandu vrea să rămână la putere cu orice preț. Toți cei 4 ani cât a fost la putere nu a îndeplinit nicio promisiune electorală. Ea înțelege că gradul de nemulțumire crește, oamenii nu o mai cred  și aveau nevoie de un element, de focuri de artificii ca să distragă atenția de la aceasta - așa au lansat acest referendum. Este o strategie de PR a Maiei Sandu din contul contribuabililor și are scopul ca oamenii să nu o întrebe ce nu s-a făcut. Scopul este ca, alegerile prezidențiale, care sunt evenimentul principal al anului, să fie mutat pe locul 3, iar principalul să fie scos în evidență referendumul. Noi, cei din opoziție, înțelegem și sperăm și oamenii din țara noastră să înțeleagă, a menționat ea. În opinia sa, chiar dacă actuala guvernare a avut instrumente și a putut pregăti terenul, prin modificarea legislației, pentru organizarea referendumului, oricum nu va putea influența dorința poporului. Dacă oamenii vor ieși masiv la vot și vor spune „nu” Maiei Sandu, rezultatele nu vor putea fi falsificate. Oamenii trebuie să iasă masiv la vot, în țară, peste hotare și să spună „nu” Maiei Sandu și „nu” referendumului. Oamenii nu sunt împotriva integrării europene, nu sunt împotriva valorile europene, ei sunt împotriva Maiei Sandu. Rezultatul referendumului din 20 octombrie va fi răspunsul oamenilor pentru atitudinea Maiei Sandu”, a precizat Irina Vlah."
    response_message = lama_response(test_prompt)
    response_message = process_string(response_message)

    print(f"Final processed response: {response_message}")
