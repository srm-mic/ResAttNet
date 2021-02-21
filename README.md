<h1 align="center"> ResCon - Team Lynx </h1>
<h3 align="center"> Residual Attention Network for Image Classification <h3>

[![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive)

![RESCON](https://user-images.githubusercontent.com/70643852/105801454-27705e80-5fbf-11eb-97c7-9cc78d4b2636.png)
<h4 align="center"> Interactions between the Feature and Attention Masks of the Residual Attetntion Network [Image Referenced from the Paper] <h4>

## Basic Model 

We have used the PyTorch-Lightning Framework to implement a Residual Attention Network which can be used for Image Classification. A Residual Attention Network is nothing but a, "Convolutional Neural Network using Attention Mechanism which can implement State-of-art feed forward network architecture", as mentioned in the abstract of the paper.

You can run the [notebook](https://github.com/AlKun25/ResAttNet/blob/main/notebook.ipynb) for testing our code.

For training the model, you have to run [train_pl.py](https://github.com/AlKun25/ResAttNet/blob/main/tools/train_pl.py)

## Observations 

| Dataset Used | Architecture implemented (Attention Type) | Optimiser Used | Image size | Training Loss | Test Loss | 
|---|---|---|---|---|---|
| CIFAR-100 | Attention-92  | SGD | 32  | 1.26 | 1.58 | 
| CIFAR-10  | Attention-92  | SGD | 32  | 0.51 | 0.53 | 
| CIFAR-100 | Attention-56  | SGD | 224 | 1.42 | 1.80 | 
| CIFAR-10  | Attention-56  | SGD | 224 | 0.61 | 0.65 | 
| CIFAR-100 | Attention-92  | SGD | 224 | 2.95 | 2.90 | 
| CIFAR-10  | Attention-92  | SGD | 224 | 1.12 | 1.01 | 

Some of the models' saved checkpoints can be downloaded from the [drive](https://drive.google.com/drive/folders/1k-rIobWZXbE5JOrBZY-0x4GO6W4aQGc9?usp=sharing)

## Further Improvements
We were able to implement only a few Res-Net architectures and that too only on 2 datasets because of the computional power and time required to run the model on our machines. Areas we are looking to improve on and work in the future
- [X] Implementing Attention-56 Architecture
- [X] Implementing Attention-92 Architecture
- [ ] Implementing Attention-128, Attention-156 Architecture
- [ ] Implementing the Paper using other Deep Learning Frameworks like Tensorflow

## Paper implemented
[Residual Attention Network for Image Classification By Fei Wang, Mengqing Jiang, Chen Qian, Shuo Yang, Chen Li, Honggang Zhang, Xiaogang Wang, Xiaoou Tang](https://github.com/AlKun25/ResCon/blob/Pranav/%5BPaper%5D%20Residual%20Attention%20Network%20for%20Image%20Classification.pdf)

## References
[ResidualAttentionNetwork-pytorch (GitHub)](https://github.com/tengshaofeng/ResidualAttentionNetwork-pytorch)
<br/>
[Residual Attention Network (GitHub)](https://github.com/fwang91/residual-attention-network)

### Citations

    @inproceedings{wang2017residual,
      title={Residual attention network for image classification},
      author={Wang, Fei and Jiang, Mengqing and Qian, Chen and Yang, Shuo and Li, Cheng and Zhang, Honggang and Wang, Xiaogang and Tang, Xiaoou},
      booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
      pages={3156--3164},
      year={2017}
    }

## Contributors

<table>
  <tr>
   <td align="center"><img src="https://github.com/harshitaggarwal01/Octahacks/blob/main/Demo%20Images%20%26%20Profiles/harshit.jfif" width="210px;" height="230px;" alt=""/><br /><sub><b>Harshit Aggarwal</b></sub></a><br />
    <p align="center">
   
   <a href="https://www.linkedin.com/in/harshit-a-46b4a0b7/" alt="Linkedin"><img src="https://raw.githubusercontent.com/jayehernandez/jayehernandez/3f5402efef9a0ae89211a6e04609558e862ca616/readme/linkedin-fill.svg"></a>
  </p>

</td>
   
   <td align="center"><img src="https://media-exp1.licdn.com/dms/image/C5603AQE_ev0fCPT0Uw/profile-displayphoto-shrink_400_400/0/1581639518725?e=1617235200&v=beta&t=AzqxcLK4xAwzH5ivzPM77rNndQ3eeg9Ac51ufXrY0-U" width="210px;" height="230px;"  alt=""/><br/><sub><b>Kunal Mundada</b></sub></a><br />
<p align="center">
    
   <a href="https://www.linkedin.com/in/kunalmundada/" alt="Linkedin"><img src="https://raw.githubusercontent.com/jayehernandez/jayehernandez/3f5402efef9a0ae89211a6e04609558e862ca616/readme/linkedin-fill.svg"></a>
  </p>
</td>
   
   <td align="center"><img src="https://media-exp1.licdn.com/dms/image/C5603AQHb5g33WP2K_Q/profile-displayphoto-shrink_400_400/0/1601352727491?e=1617235200&v=beta&t=U3K08OW14cdA7JltrCiBf9v2-YNp3q-MYglbNMbiPBg" width="240px"; height="230px;" alt=""/><br /><sub><b>Pranav B Kashyap</b></sub></a><br />
<p align="center">
   
   <a href="https://www.linkedin.com/in/pranav-b-kashyap-1994001b6/" alt="Linkedin"><img src="https://raw.githubusercontent.com/jayehernandez/jayehernandez/3f5402efef9a0ae89211a6e04609558e862ca616/readme/linkedin-fill.svg"></a>
  </p>
</td>
    </tr>
    </table>
