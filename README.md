<span style="color:red">**Notes:**</span>
* Any functions that contain parameters have `TP mode` - (Test Params) .<br />
To activate `TP mode` you just need pass `mode="TP"` to the function. <br />
For example:
```python
rotate_remain_bound(image, -3, mode="TP")
```

* To show results pass `show=True` to the function. <br />
For example:
```python
rotate_remain_bound(image, -3, show=True)
```

### Commons
1. resize_by_size
2. resize_by_factor
3. rotate_by_direction
4. rotate_by_angle
5. rotate_remain_bound

### Requirements
1. OpenCV - [install](https://pypi.org/project/opencv-python/)
2. Numpy - [install](https://pypi.org/project/numpy/)