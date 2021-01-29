# Voting in a Watts-Strogatz Small-World-Network

In this research project we simulated a two party majority voting scheme in a Wattz-Strogatz world network. Three different types of voting function were implemented and the results were compared.

### Abstract :
Social network science and social interaction science is an interesting and steadily growing field of research in current time. Social network influences the lives of millions, and therefore the propagation of influence in such a network deserves study. In this paper, we have studied voting in a Watts-Strogatz small world network for two parties. In our model, each node has an initial bias towards one of the parties (or can be neutral) and are
influenced by their neighbours to vote for a particular party. 
We show via simulation that 
(i) for linear of logarithmic voting function, the small scale variation is minimum, but the majority of the nodes tend to align towards one of the parties in the long term 
(ii) for periodic voting function, the small scale variations are sharp and oscillating, but in the long term the number of voters in each party roughly remains the same, 
(iii) the degree of the graph does not seem to have a strong influence on the result, and 
(iv) networks with higher small world probability tend to resist the alignment of voters towards a particular party for a longer time as compared to networks with lower small world probability. This majority voting model seems to efficiently capture the potential behaviour of voters on small world network over a campaigning period.

### Find the full paper [here](https://link.springer.com/chapter/10.1007/978-981-15-7834-2_31)

## The Components

### Watts-Strogatz Small World Network
![](https://github.com/thecrazyphysicist369/Voting-in-a-Small-World-Network/blob/master/swn.png)
This is a special type of graph, a small world, which depicts the human dynamics of real world in a fundamental level without all the real world abstractions.
Watts-Strogatz small world network uses 3 variables to define the network.

1. ***Nodes              =  n***   _The total number of nodes in the Small World_
2. ***Nearest neighbors  =  k***   _The number of nodes each node is connected to. Also called nearest-neighbors_
3. ***Probability        =  p***   _This is the length of connection of the edges_

### Voting Function
```
bnew = b + ∑ sign(i)*f(w(i,j))
```

#### 1. Linear Voting Function
```
f ( (w (i, j))  =  w (i, j)
```
The modification to an individuals' bias is depended linearly on the influence value of the influencer.

#### 2. Logarithmic Voting Function
```
f ( (w (i, j))  =  log (w (i, j))
```
The modification to an individuals' bias is dependent logarithmically on the influence value of the influencer.

#### 3. Periodic Voting Function
```
f ((w (i, j))  =  sin (w (i, j))
```
The modification to an individuals' bias is dependent periodically on the influence value of the influencer.


## Executing the Code

### Prerequisites

As this code is in the form of Google Colaboratory Notebook, you can start running the code straight from the browser. But if you're willing to run the code locally, you'd be needing the following packages
```
networkx
matlplotlib
```



### The Election

Two ways to obtain output 

#### 1. Value Inputs

Explain what these tests test and why

```
Population : 
Nearest-Neighbor : 
Probability : 
Voting-Function : 
Iterations : 
```

#### 2. Slider

Explain what these tests test and why

```
Give an example
```

## Results
### Linear Voting

```
Describing Linear Voting results.
```
![P,K](https://github.com/thecrazyphysicist369/Voting-in-a-Small-World-Network/blob/master/Images/Lik5p5.png)

### Logarithmic Voting

```
Describing Logarithmic Voting resutls.
```
![P,K](https://github.com/thecrazyphysicist369/Voting-in-a-Small-World-Network/blob/master/Images/Lok5p5.png)

### Periodic Voting

```
Describing Periodic Voting results.
```
![P,K](https://github.com/thecrazyphysicist369/Voting-in-a-Small-World-Network/blob/master/Images/Prk5p5.png)












## Built With

* [Python-3](https://www.python.org/) - The language.
* [Networkx](https://matplotlib.org/) - The network generating library.
* [Matplotlib](https://networkx.org/) - The plotting-visualising library.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Shaun** - *Implementation and Code* - [Twitter](https://twitter.com/thecrzyphysicst), [Google Scholar](https://scholar.google.com/citations?hl=en&user=mxc8IfcAAAAJ)
* **Dr. Debayan Ganguly** - *Co-authored* - [The Crazy Physicist](https://twitter.com/thecrzyphysicst)


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
