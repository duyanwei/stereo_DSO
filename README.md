# stereo_dso

**Dec-26-2022**

The codebase was originally from https://github.com/RonaldSun/stereo_DSO, thanks the author \<Ronald Sun\> for the implementation and making it public.

A few modifications have been made:
- Make it work with EuRoC dataset (probably won't work with kitti anymore)
- Save tracking and mapping stats, including time cost
- Save tracking and mapping pose estimation result

---
# stereo_DSO

## Related Papers:

- **Direct Sparse Odometry**, *J. Engel, V. Koltun, D. Cremers*, In arXiv:1607.02565, 2016
- **Stereo DSO:Large-Scale Direct Sparse Visual Odometry with Stereo Cameras**, *Rui Wang, Martin Schwörer, Daniel Cremers*, 2017 IEEE International Conference on Computer Vision

## Experiments

- kitti00:

![](https://github.com/RonaldSun/stereo_DSO/blob/master/results/img/00.png)

![](https://github.com/RonaldSun/stereo_DSO/blob/master/results/img/00_tl.png)

![](https://github.com/RonaldSun/stereo_DSO/blob/master/results/img/00_rl.png)
