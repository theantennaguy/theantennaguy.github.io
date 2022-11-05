
layout: post
title: Active GNSS antenna design (Part III)
draft: true


Alright, welcome to the third and last post about the generation I Active GNSS antenna design saga. In this one I'll post about the actual results obtained from the constructed antenna. But first, I'll briefly explain something I forego in my previous two posts concerning the impedance match of the amplifier and was asked by a friend who happen to read this blog.

The input matching of the LNA designed in the previous posts is pretty miserable, and I really didn't care to match it to 50 $\Omega$ and was solely concerned to match it to the lowest possible NF. Now, it's common to have LNAs with input and output matching to 50 $\Omega$, and that is generally the best practice. This is very relevant since the LNAs can be integrated with band-pass filters at input and/or output, and these filters are usually designed for an input and output impedance of 50 $\Omega$, and when this is not the case, that can change the frequency response of the filter and completely alter its expected performance, hence ruining the receiver. In my particular case, there's no filter, the antenna is directly driving the LNA, so the input matching is less critical. Now, of course, having a high input return loss will reflect the signal back to the antenna and may cause other sources of disturbance, cause de-polarization (remember I'm expecting RHCP and I have a hybrid square guiding those signals tightly), the reflected signal can cause destructive interference with incoming signals and the most obvious reduce the amount of power being delivered to the LNA for amplification. The former two impairments are very hard to predict, but the last one, it can be determined from the matching loss

$$
ML_{dB}=-10 \times log_{10}(\frac{1}/{(1-\|S_{11}\|^2)})
$$

*remember the $\|S_{11}\|$ is in linear form*

In this case, from simulations we're looking at a return loss of -4 to -5 dB, which translates to 1.651 to 2.205 dB of matching loss. We can live with that given the 26 dB of theoretical gain we're expecting from the amplifier.

Before moving on to the measured results, here's some nice pictures of the fabricated PCBs of the antenna and the LNA.

|![antpcb](/images/post15/antenna_pcb.png)|![lnapcb](/images/post15/lna_pcb.png)|
|:-------------------------:|:-------------------------: |
|Ring antenna PCB | LNA PCB |





Having this completed I had some ideas on how to improve this antenna, making it more compact and having more active gain, therefore,  I'll keep posting more updates on GNSS antennas in the future. I have an upgrade for the LNA board design, and I'm working on a new, more compact version of the radiating element!

I'll try to diversify, and my next post will be about something different than GNSS, but I'll come back to GNSS in the future for sure.

So stay tuned folks!