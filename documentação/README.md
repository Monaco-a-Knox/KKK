Este documento se refere exclusivamente ao processo de compilação de KKK, baseado nos arquivos e estrutura deste patch.
Explicações rápidas e pouco detalhadas.

Para uma documentação detalhada sobre a engine MalieSystem, verifique o repositório de [Dies Irae](https://github.com/Monaco-a-Knox/Dia-da-Ira/tree/main/outros).

O script para tradução está localizado em ```malie tools\compilar\[...]\data```

Mova-o para ```KKK\dependencies\script``` e renomeie para ```message.txt```
Este é o arquivo onde a tradução deve ser trabalhada.

Sempre que forem feitas modificações ou você quiser gerar um novo patch, o primeiro passo é rodar ```wordwrap.py``` e uma cópia com as quebras de linhas será criado em ```KKK\dependencies\script_done```.
Você pode modificá-lo para ajustar o número de caracteres por linha. Atualmente em 25.

O próximo passo é mover este arquivo com as quebras para a pasta ```data``` localizado dentro da estrutura do ```malie tools\compilar\[...]\data```.
Nesta pasta estarão também o arquivo com as escolhas ```exec.str.txt``` e o arquivo ```exec.org.dat```

Você precisará renomear seu script novamente para ```exec.msg.txt``` e então rodar o ```Malie_Script_Tool.exe```, gerando um novo ```exec.dat``` na pasta ```.data``` (**ponto data**).

Agora mova o arquivo para ```data\system``` e rode ```dat_pack.py``` indicando que você quer compilar a pasta ```data```.

Isso resultará no patch ```data6.dat``` que vai surgir na pasta raiz do repositório. Mova-o para ```[KT] KKK```e "zipe" a pasta, finalizando seu patch.

Nesta pasta também estão os arquivos ```malie.ini```, que contém a tradução do título do jogo na janela e a indicação de fonte tamanho 18pt, permitindo mais caracteres na caixa vertical.
Se você quiser o patch no com caixa horizontal ou modo nvl, utilize o tamanho original 20pt. Para que funcione corretamente, siga as orientações sobre mudar o sentido do texto e editar a caixa, presentes no primeiro link.

Também há um arquivo executável do jogo, que permite rodá-lo sem precisar do AlphaROMdiE. [Cortesia do Cosetto](https://github.com/Monaco-a-Knox/KKK/tree/main/%5BKT%5D%20KKK).

----

Há duas diferenças entre esse processo e a copilação de Dies Irae, na qual é automatizada. Verificar [compile_pc.py](https://github.com/Monaco-a-Knox/amantesamentes/blob/main/dependencies/compile_pc.py) e [compile_pc.yml](https://github.com/Monaco-a-Knox/amantesamentes/blob/main/.github/workflows/compile_pc.yml).

Em Dies Irae, a compilação e decompilação do script é feita com o ```StringTool.exe```. Ele é mais prático e simples, mas não permite adicionar ou remover rubys, nem adicionar quebras e é péssimo para exibir texto japonês justamente pelos motivos citados.
Ele poderá ser utilizado caso finalize a tradução e descubra uma maneira de quebrar as linhas automaticamente, assim eliminamos o uso do ```malie tool``` e do ```wordwrap.py```, podendo reutilizar a compilação automática já existente, mudando somente o nome dos arquivos e pastas.

É importante frisar que arquivos compilados com o Malie Tool pode deixar de ser compatíveis com o StringTool após editar o ```exec.str.txt```. Se possível, faça a tradução deste antes de tudo, utilizando a tecla "insert".
Essa incompatibilidade pode dar muita dor de cabeça, mas é possível superá-la fazendo as coisas na ordem correta e não voltando para fazer novas modificações após conseguir. Isto, claro, se descobrir como quebrar as linhas automaticamente. Possivelmente está relacionado com o próprio ```.exe``` do jogo.

----

Para criação de imagens das cartas, rodar os scripts ```tegami.py```, localizado na pasta ```tgm```.

Após criar as imagens, movê-las para ```KKK\data\picture\event```

Não há script para criação automática de outras imagens.

----

Se quiser trocar a fonte e melhorar o kerning, [verifique](https://github.com/Akaruzi/kkk_r18_patch/tree/master/entrans/wordwrap)

----

Não há como utilizar a quebra de linha em texto sobreescrito (ruby). O ideal seria uma caixa horizontal para adicioná-lo nas runas, mas isso estragaria a estética do jogo.
Boa sorte lidando com isso e/ou descobrindo como fazer o jogo quebrar linhas automaticamente, tal qual ocorre na versão inglesa de Dies Irae. Isso resolveria todos os problemas e facilitaria o processo de compilação.