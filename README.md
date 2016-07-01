# HuffmanCoding

KSA DS&Algorithm1 first assignment: Compressing text files using Huffman coding algorithm.

Credit: 13-142 한동규

## Download

git이 설치되어 있다면 다음 명령어로 다운로드할 수 있습니다.

    git clone https://github.com/dongq98/HuffmanCoding.git

다른 방법으로는, 본 [깃허브 페이지](https://github.com/dongq98/HuffmanCoding)에서 Clone or download - Download ZIP 버튼을 눌러 다운로드할 수 있습니다.

## Running the code

다음 명령어를 통해 프로그램을 실행할 수 있습니다.

    python Main.py

## How to use

### Compression

File input 인터페이스의 open 버튼을 눌러 압축할 파일을 열 수 있습니다.
압축할 파일이 열리면 위쪽 텍스박트스에 압축할 파일의 내용이 출력됩니다.
Compress! 버튼을 누르면 압축이 진행되며, 압축된 파일의 내용이 아래쪽 텍스트박스에 출력됩니다.
압축된 파일의 허프만 트리는 왼쪽 캔버스에 그려집니다.
압축된 파일과 허프만 코드북은 각각 *.comp, *.huff 형식으로 출력됩니다.
Compress! 버튼의 바로 아래에는 압축률이 표시됩니다.

### Decompression

File input 인터페이스의 open 버튼을 눌러 압축된 파일과 허프만 코드북을 열 수 있습니다. 출력 위치는 앞서 설명한 것과 동일합니다. Decompress! 버튼을 누르면 압축 해제가 진행되며, 위쪽 텍스트박스에 원본 텍스트 파일이 출력됩니다. 원본 텍스트 파일은 *.dcmp 형식으로 출력됩니다.

## Trivia

* 본 프로그램은 실제 압축 프로그램이 아닌 실습용 프로그램으로서, 압축 결과가 비트의 나열이 아닌 0과 1로 이루어진 스트링이기 때문에 파일 용량이 더 커집니다.
* 또한 허프만 코드북이 한 파일에 함께 출력되는 것이 아니므로 실제 압축 프로그램으로 쓰기에는 부적합합니다.
* 하지만 뛰어난 압축률을 보이므로 프로그램을 수정하면 실제 압축 프로그램으로 사용 가능할 것입니다.
