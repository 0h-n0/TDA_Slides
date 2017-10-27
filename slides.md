name: inverse
layout: true
class: center, middle, inverse
---
# Introduciton to TDA
#### 28/10/2017
#### Koji Ono

--
 
#### My major was Biology.

--

#### So I'm not familiar with Mathmatics...
---
layout:false
name: agenda

## Agenda

### 1. What is TDA? (Overview of TDA)

### 2. Application.

### 3. Homology.

### 4. Persistent Homology.

### 5. Let's caluculate Homology.

### 6. References

---
## 1. What is TDA? (Overview of TDA)

**TDA** stands for **T**oplogical **D**ata **A**nalysis

- ".red.bold[Topological]" means ...
    - Differential topology.
    - Geometric topology.
    - Homotopy theory.
    - Homology.
    - etc.

--

These mathematical methods are for analyzing **phase**. 

--

To find out "Topological Invariant.
    

---
## 1. What is TDA? (Overview of TDA)

.emphasize[One of the machine learning method.]

.left-column[
### Supervised
- Nerural Network
- SVN
- Bayeasian
- etc.

]

--

.right-column[
###Unsupervised
- PCA
- Clustering(hierachical)
- Clustering(non-hirerarchical)
- etc.
]

???
![Default-aligned image](https://i.ytimg.com/vi/TDL8WbnBvyo/hqdefault.jpg)

--

**TDA** is similar to Clustering(non-hirerarchical method)

---
## 1. What is TDA? (Overview of TDA)

#### Random data

.center[
<video preload="auto" width="70%" height="auto" data-setup="{}" loop controls><source src="https://github.com/0h-n0/TDA_Slides/blob/images/src/random.mp4?raw=true" type="video/mp4" /></video>
]

--- 
## 1. What is TDA? (Overview of TDA)

#### Cicle data 

.center[
<video preload="auto" width="70%" height="auto" data-setup="{}" loop controls><source src="https://github.com/0h-n0/TDA_Slides/blob/images/src/random.mp4?raw=true" type="video/mp4" /></video>
]

---
## 2. Application.

There are A lot of Application of TDA in Bioloby.

* Sensor-network coverage
* Proteins
* 3-dimensional sturecture of DNA
* Development of cells
* robotics
* signals in images
* ...

---

## 3. Homology.

###  Defintion of Homology Group.

$$H_k(K) = Z_k(K) / B_k(K)$$


---

## 3. Homology.

####  Simple Complex

$$H_k(K) = Z_k(K) / B_k(K)$$


---

## 4. Persistent Homology.

###  Defintion of Persistent Homology Group.

For finite filltration of simple complex

    
$${\mathbb K} : \subset K^0 \subset K^1 \cdots \subset K^t \subset \cdots$$

, k-dimension Persistent Homology Group is



$$PH_k({\mathbb K}) = Z_k({\mathbb K}) / B_k({\mathbb K})$$

---

## 5. Let's caluculate Homology.

---


## 6. References 1
### Group Theory
- https://www.youtube.com/watch?v=VdLhQs_y_E8
    - Harvard lecture videos about abstract algebra on Youtube.
- 『代数学１、２、３』　雪江　明彦著
    - Japanese good reference book about abstract algebra.
    
### Homology
- https://www.youtube.com/watch?v=EA1FFtTGAfw
    - American university's lecture videos about introduction and application of homology on Youtube.
- 『タンパク質構造とトポロジー ―パーシステントホモロジー群入門― (シリーズ・現象を解明する数学)』　平岡 裕章著
    - Japanese book about application of persistent homology to biology.
- 『A roadmap for the computation of persistent homology』(2015) Nina et. al.
    - Good review.
- 『Computational Homology (Applied Mathematical Sciences)』(2004)
    - There are a lot of information that homology is applied for image data.

---
## 6. References 2
### Homology
- 『Elementary Applied Topology』(2014)
    - It is said that this book is good, but I don't know well.
- 『計算で身につくトポロジー』 阿原 一志著
    - This is one of the book I want.
    
---
## 7. Book list

- コホモロジーのこころ
- ホモロジー代数　河田
- 代数的トポロジー
- トポロジー　田村
