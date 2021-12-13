# Allium

> _Allium_: a genus of monocotyledonous flowering plants to which onion species belongs.

Allium is a prototype implementation of the [Riffle](https://people.csail.mit.edu/devadas/pubs/riffle.pdf) anonymity network.
 
Currently, this project is being made **for study purposes only**, therefore, **it should not be used for any real anonymous communication.**

## How Allium works?

First, it is necessary to define the concepts of **Onion Routing** and **Mixnets**.

[Onion Routing](https://en.wikipedia.org/wiki/Onion_routing) is a technique that aims at the anonymity of communication between a computer network. For this, messages are encapsulated in encryption layers, hence the name onion routing, referring to the layers of an onion. The image below shows a message being sent with onion routing.

![Onion routing representation](https://upload.wikimedia.org/wikipedia/commons/e/e1/Onion_diagram.svg)

[MixNets](https://en.wikipedia.org/wiki/Mix_network) are routing protocols designed to make it difficult to track any message. They work as follows:

- The message, already encrypted in layers, is sent to the first MixNet server;
- Upon receiving this message, the server decrypts the first layer, and shuffles the order of the messages. After shuffling, send messages to the next server;
- The second server receives the messages, decrypts the second layer, shuffles the order of the messages, and sends them to the next server;
- Finally, the last server receives the messages, decrypts the last layer, and sends them to the receiver.

![MixNets representation](https://upload.wikimedia.org/wikipedia/commons/4/4f/Red_de_mezcla.png)

One of the problems found in MixNet is that the receiver is not anonymous, and if one of the servers is malicious, the anonymity of the sender is also compromised. To solve this, the Riffle protocol was developed.

## Private Information Retrieval (PIR)
In Riffle we can use the Private Information Retrieval (PIR) method, so that users can access servers anonymously, obtaining information from the servers without the servers being notified of this access and what information we were looking for.
The PIR can be used to solve problems on servers with small storage, borrowing all the information from the servers so that we can carry out a query without the server's knowledge, thus maintaining the privacy of a search.
