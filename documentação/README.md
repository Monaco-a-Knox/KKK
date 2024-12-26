#Compilação

Este do documento refere-se exclusivamente ao processo de compilação de KKK, baseado nos arquivos e estrutura deste patch.

Para uma documentação detalhada sobre a engine MalieSystem, verifique o repositório de (Dies Irae)[https://github.com/Monaco-a-Knox/Dia-da-Ira/tree/main/outros].

----

O arquivo com a tradução ```message.txt``` encontra-se na pasta ```KKK\dependencies\script```.
Este é o arquivo onde a tradução deve ser trabalhada.

Este arquivo nada mais é do que o arquivo ```exec.msg.txt``` renomeado.

Sempre que forem feitas modificações ou você quiser gerar um novo patch, o primeiro passo é rodar ```ww.py``` e uma cópia com as quebras de linhas será criado em ```KKK\dependencies\script_done```

O próximo passo é mover este arquivo com as quebras para a pasta ```data``` localizado dentro da estrutura do ```malie tools\compilar\[...]\data```.
Nesta pasta estarão também o arquivo com as escolhas ```exec.str.txt``` e o arquivo ```exec.org.dat```

Você precisará renomear seu script para ```exec.msg.txt``` e então rodar o ```Malie_Script_Tool.exe```, gerando um novo ```exec.dat``` na pasta ```.data``` (**ponto data**).

Agora mova o arquivo para ```data\system``` e rode ```dat_pack.py``` indicando que você quer compilar a pasta ```data```.

Isso resultará no patch ```data6.dat``` que vai surgir na pasta raiz do repositório. Mova-o para ```[KT] KKK```e "zipe" a pasta, finalizando seu patch.

Nesta pasta também estão os arquivos ```malie.ini```, que contém a tradução do título do jogo na janela e a indicação de fonte tamanho 16pt, permitindo mais caracteres na caixa vertical.
Se você quiser o patch no com caixa horizontal ou modo nvl, utilize o tamanho original 20pt. Para que funcione corretamente, siga as orientações sobre mudar o sentido do texto e editar a caixa, presentes no primeiro link.

Também há um arquivo executável do jogo, que permite rodá-lo sem precisar do AlphaROMdiE. [Cortesia do Cosetto](https://github.com/Akaruzi/dies_aitrans/files/15236486/malie.zip).

----

Há duas diferenças entre esse processo e a copilação de Dies Irae, na qual é automatizada. Verificar [compile_pc.py](https://github.com/Monaco-a-Knox/Dia-da-Ira/blob/main/dependencies/compile_pc.py) e [compile_pc.yml](https://github.com/Monaco-a-Knox/Dia-da-Ira/blob/main/.github/workflows/compile_pc.yml).

Em Dies Irae, a compilação e decompilação do script é feita com o ```StringTool.exe```. Ele é mais prático e simples, mas não permite adicionar ou remover rubys, nem adicionar quebras e é péssimo para exibir texto japonês justamente pelos motivos citados.
Ele poderá ser utilizado caso finalize a tradução e descubra uma maneira de quebrar as linhas automaticamente, assim eliminamos o uso do ```malie tool``` e do ```wordwrap.py```, podendo reutilizar a compilação automática já existente, mudando somente o nome dos arquivos e pastas.

É importante frisar que arquivos compilados com o Malie Tool pode deixar de ser compatíveis com o StringTool após editar o ```exec.str.txt```. Se possível, faça a tradução deste antes de tudo, utilizando a tecla "insert".
Essa incompatibilidade pode dar muita dor de cabeça, mas é possível superá-la fazendo as coisas na ordem correta e não voltando para fazer novas modificações após conseguir. Isto, claro, se descobrir como quebrar as linhas automaticamente. Possivelmente está relacionado com o próprio ```.exe``` do jogo.

----

Para criação de imagens, rodar ```epic_2.py```, localizado na pasta ```tgm```. No momento, ele só está configurado para a primeira carta.

p1 = [5, 5, 5, 5, 5, 5, 6, 6, 9, 5]
p1_s = [0, 5, 10, 15, 20, 25, 30, 36, 42, 51]

p1 indica q quantidade de linhas a cada "cena", isto é, antes de limpar e iniciar uma nova página.
p1_2 indica a quantidade total de linhas na carta, separando elas por página.

Basta seguir essa mesma lógica nas demais cartas.