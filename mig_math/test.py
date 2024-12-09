def do_one_iter(bw, remain_mem, dirtyrate, delta):
    new_remain_mem = remain_mem + dirtyrate  * (delta / 1000)
    return new_remain_mem

def get_total_time_all(bw: float, total_mem: float, downtime: float, dirtyrate: float):
    remain_mem = total_mem
    iter_time = 0
    delta = 0
    total_time = 0
    while True:
        if downtime * dirtyrate / 1000 > remain_mem:
            remain_mem=do_one_iter(bw, remain_mem, dirtyrate, delta)
            iter_time +=1
            #print("iter_time:", iter_time, "remaining:", remain_mem, "total_time:", total_time)
            if downtime * dirtyrate / 1000 > remain_mem:
                break
            delta=0
        delta += 100
        total_time += 100
        ## print(delta)
        remain_mem -=  bw* 100 / 1000;

    return total_time

if __name__ == "__main__":
    bw = 90 * 1024 / 8  # 11.25 GB/s
    bw = 11760
    
    total_time = get_total_time_all(bw, 327680, 300, 10240)
    print(total_time)
    total_time = get_total_time_all(bw, 327680, 300, 10240)
    print(total_time)

