from Tkinter import *

master = Tk()
w = Canvas(master, width=300, height=300, bg='black')
w.pack(expand=YES, fill=BOTH)
points = [424.59299999999996, 605.412, 434.756, 600.5305, 445.935, 603.5275, 489.634, 600.7465, 501.82950000000005, 606.7, 546.5445, 600.9705, 592.2764999999999, 596.2295,
          659.3495, 554.1700000000001, 698.9834999999999, 479.52349999999996, 706.0974999999999, 354.55100000000004, 680.6905, 286.5375, 627.8455, 237.11749999999998, 571.951,
          221.1495, 508.943, 209.09050000000002, 477.43899999999996, 205.02949999999998, 445.935, 204.9055, 426.626, 208.766, 385.9755, 209.59050000000002, 301.626,
          235.83300000000003, 244.71550000000002, 285.806, 221.3415, 345.75350000000003,
          221.3415, 454.0210000000001, 247.76399999999998, 531.8805, 292.4795, 581.2695, 345.325, 603.1305, 393.08949999999993, 604.3035, 424.59299999999996, 605.412]

w.create_polygon(points, fill='orange', width=2)
stem = [501.82950000000005, 201.36099999999996, 489.634, 207.3145, 445.935, 204.53349999999998, 434.756, 207.5305, 424.59299999999996, 202.64899999999994, 427.64250000000004, 189.84199999999998,
        437.80500000000006, 167.164, 420.5285, 121.95649999999995, 443.90250000000003, 108.08499999999998, 474.39, 169.973, 501.82950000000005, 201.36099999999996]

w.create_polygon(stem, fill='green', width=2)
eye1 = [429.675, 422.5565, 370.7315, 430.6625, 383.943, 419.784, 381.91, 400.10699999999997, 361.5855, 389.36, 345.325, 389.424, 330.0815, 406.217, 340.244, 428.81399999999996, 301.626, 411.2495, 300.60949999999997,
        377.789, 317.886, 349.178, 354.471, 327.38, 361.5855, 355.89549999999997, 429.675, 422.5565]

w.create_polygon(eye1, fill='red', width=2)
eye2 = [494.7155, 421.06, 527.236, 398.2945, 558.74, 369.627, 571.951, 327.252, 613.618, 355.6315, 624.7965, 372.32000000000005, 623.7805000000001, 411.694, 587.1949999999999, 425.61800000000005,
        594.309, 401.968, 571.951, 386.3075, 549.593, 396.23800000000006, 543.496, 414.96250000000003, 552.6424999999999, 429.69050000000004, 494.7155, 421.06]
mouth = [275.7724, 458.8808, 333.496, 472.82640000000004, 360.3252, 546.7368, 392.8456, 483.61640000000006, 500.1628, 483.98160000000007, 533.496, 547.6296, 561.1384, 474.29240000000004, 627.8048, 459.06960000000004, 613.9836, 510.3052, 576.5852, 562.4208000000001, 505.0408, 598.9228, 487.9676, 573.0060000000001, 477.39840000000004,
         604.5436, 422.11400000000003, 603.9736, 411.5448, 573.3068000000001, 392.8456, 600.152, 331.0568, 568.1116000000001, 287.9676, 510.80120000000005, 275.7724, 458.8808]

w.create_polygon(eye2, fill='red', width=2)
w.create_polygon(mouth, fill='red', width=2)
text = w.create_text(730,730, text="Happy Halloween!!!", fill="purple", font=("Helvectica", "20"))
mainloop()
