# HuffmanCoding
KSA DS&Algorithm1 first assignment: Compressing text files using Huffman coding algorithm.  
Credit: 13-142 한동규

## 실행 결과
### 압축

Flying Spaghetti Monster 위키피디아 항목의 일부를 압축하였다.  
해당 텍스트 파일은 examples 폴더에 위치해 있다.
![Huffman1](https://github.com/dongq98/HuffmanCoding/blob/master/screenshots/Huffman1.png)
![Huffman2](https://github.com/dongq98/HuffmanCoding/blob/master/screenshots/Huffman2.png)
압축률은 약 55.3%로 압축이 잘 되었다.

### 압축 해제

위에서 압축한 파일을 다시 압축 해제하였다.
압축 해제에 이용한 .comp, .huff 파일은 examples 폴더에 위치해 있다.
![Huffman3](https://github.com/dongq98/HuffmanCoding/blob/master/screenshots/Huffman3.png)
![Huffman4](https://github.com/dongq98/HuffmanCoding/blob/master/screenshots/Huffman4.png)
원본 텍스트 파일과 동일한 결과가 나왔음을 알 수 있다.

## 이론 및 분석

Huffman coding은 entropy encoding의 한 종류이다. Huffman coding에는 다음과 같은 성질이 있다.
* 무손실 압축이다. 
* [Optimal하다.](http://www.cs.utoronto.ca/~brudno/csc373w09/huffman.pdf)
  즉, Huffman coding을 통해 계산한 prefix code를 이용했을 때 가장 압축률이 좋다.

[Shannon's source coding theorem](https://en.wikipedia.org/wiki/Shannon%27s_source_coding_theorem)에 따르면,
Huffman coding의 optimality로부터 각 codeword 길이가 글자 빈도의 음의 로그 `-log(P)`에 거의 비례함을 알 수 있다.

실제로 글자 빈도가 가장 높은 e가 Huffman tree에서 가장 depth가 작았고 (즉, codeword 길이가 짧았고)
그 다음으로 빈도가 높은 a, i, n, o, r, s, t 등도 depth가 작게 나타났다.
