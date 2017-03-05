import sys, time


class ProgressBar:
    def __init__(self, count=0, total=0, width=50):
        self.count = count
        self.total = total
        self.width = width

    def move(self):
        self.count += 1

    def log(self):
        # sys.stdout.write(" " * (self.width + 10) + "\r")
        # sys.stdout.flush()
        progress = self.width * self.count / self.total
        # sys.stdout.write("{0:3}/{1:3}: ".format(self.count, self.total))
        sys.stdout.write(">" * int(progress) + "-" * (self.width - int(progress)) + "\r")
        if progress == self.width:
            sys.stdout.write("\n")
        sys.stdout.flush()


bar = ProgressBar(total=10)
for i in range(10):
    bar.move()
    bar.log()
    time.sleep(1)
