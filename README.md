# Trabalho-Vinicius


1. Geração de números (gerar_numeros)

	Gera um arquivo chamado numeros_grandes.txt.

	Preenche o arquivo com números aleatórios entre 0 e 1.000.000.000.

	O tamanho final do arquivo pode chegar a 1 GB ou mais, dependendo do parâmetro informado.

	Exibe o tamanho aproximado do arquivo em MB.

2. Ordenação dos números (ordenar_numeros)

	Carrega o arquivo numeros_grandes.txt.

	Ordena todos os números na memória usando .sort().

	Salva o resultado em numeros_ordenados.txt.

 3. Movimento dos arquivos para a Área de Trabalho (mover_para_area_trabalho)

	Move automaticamente:

	numeros_grandes.txt

	numeros_ordenados.txt

	Ambos são enviados para a Área de Trabalho do usuário (Windows, Linux ou macOS).

Como executar
	1. Certifique-se de ter o Python instalado

Versão recomendada: Python 3.9+

	2. Salve o arquivo com extensão .py

Por exemplo:

gerador_ordenador.py

3. Execute no terminal
	python gerador_ordenador.py

	Parâmetros importantes
	gerar_numeros(tamanho)

	O parâmetro tamanho representa o tamanho do arquivo em bytes.

	Exemplo para gerar 1 GB:

	gerar_numeros(1 * 1024**3)

Observação importante

	O método .sort() carrega todo o arquivo em memória RAM.
	Para arquivos muito grandes, isso pode exigir 4–8 GB de RAM.

	Estrutura dos arquivos gerados

	Após executar o programa, você terá:

	Desktop/
	 ├── numeros_grandes.txt        # números aleatórios
	 └── numeros_ordenados.txt      # números ordenados

Cuidados

	Gerar arquivos grandes consome bastante tempo, RAM e espaço em disco.

	Ordenar 1 GB de números pode demorar vários minutos dependendo do hardware.

	Em computadores com pouca memória, o processo pode causar lentidão.
