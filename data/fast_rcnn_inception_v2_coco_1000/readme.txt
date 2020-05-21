1. frozen_inference_graph.pb.tmp.best
2020年05月21日08:47:44
到目前位置最好的模型，几乎没有误识别，就是采样帧率有点低。
与楼顺凯一起测试过的扔球模型。

2. frozen_inference_graph.pb.60k
训练6w步之后的模型，1.2 -3 米之内识别的效果最好，4米左右，有时会识别不到。
此模型比第一个模型，多训练了步数。

3. frozen_inference_graph.pb.without1
一个有误识别的模型，但是远距离识别的快速性，要比第一个与第二个都好。
白色北京略有丢帧

