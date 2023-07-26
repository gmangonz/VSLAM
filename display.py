
    # Gy = H // 8 #12 // 2
    # Gx = W // 8# 16 // 2
        # sy = img.shape[0]//self.Gy
        # sx = img.shape[1]//self.Gx
        # akp = []
        # for ry in range(0, img.shape[0], sy):
        #     for rx in range(0, img.shape[1], sx):
        #         patch = img[ry:ry+sy, rx:rx+sx]
        #         kp = self.orb.detect(patch)
        #         for p in kp:
        #             p.pt = (p.pt[0]+rx, p.pt[1]+ry)
        #             akp.append(p)
        # return akp