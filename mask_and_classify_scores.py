import numpy as np

def mask_and_classify_scores(arr):
    if type(arr) is not np.ndarray:
        return None
    
    if arr.ndim !=2 or arr.shape[0] != arr.shape[1]:
        return None
    
    n = arr.shape[0]
    if n<4:
        return None
    
    cleaned = arr.copy()
    cleaned[cleaned < 0] = 0
    cleaned[cleaned > 100] = 100
    
    levels = np.zeros(cleaned.shape , dtype=int)
    levels[cleaned < 40] = 0
    levels[(cleaned >= 40) & (cleaned < 70)] = 1
    levels[cleaned >= 70 ] = 2
    
    row_pass_counts = np.zeros(n, dtype=int)
    for i in range(n):
        count = 0
        for value in cleaned[i]:
            if value >= 50:
                count += 1
        row_pass_counts[i] = count
        
    return (cleaned , levels , row_pass_counts)

scores = np.array([
    [120,50,-5,80],
    [30,60,75,40],
    [55,20,90,110],
    [10,70,65,45],
    ])

result = mask_and_classify_scores(scores)

if result is not None:
    cleaned,levels,row_pass_counts = result
    print("cleaned:")
    print(cleaned)
    print("Levels:")
    print(levels)
    print("Row pass count:")
    print(row_pass_counts)
else:
    print("Invalid Input")
