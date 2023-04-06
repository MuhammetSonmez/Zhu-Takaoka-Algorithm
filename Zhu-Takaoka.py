def zhu_takaoka(path):
    points = list(range(len(path)))
    #points listesi, path indislerini içeren bir listeye atanır.
    key = []
    #anahtar listesi başlangıçta boş bir değer olarak atanır
    while len(points) > 0:
        leftmost_point = min(points)
        #leftmost_point, anahtar listesine eklenir.
        key.append(leftmost_point)
        # leftmost_point'tan daha büyük olan tüm elemanlar points listesinden çıkarılır.
        points = [p for p in points if p > leftmost_point]
        #path[leftmost_point]'den daha büyük olan tüm elemanlar right_points listesine atanır.
        right_points = [p for p in points if path[p] > path[leftmost_point]]
        # right_points listesi boş değilse,
        if len(right_points) > 0:
            # rightmost_point, right_points listesindeki en küçük elemanı alır.
            rightmost_point = min(right_points)
            key.append(rightmost_point)
            # rightmost_point, anahtar listesine eklenir.
            points = [p for p in points if p < rightmost_point]
            # rightmost_point'tan küçük olan tüm elemanlar points listesinden çıkarılır.
    return key # Anahtar listesi döndürülür.

def zhu_takaoka_for_inputs(inputs):
    key = []
    # Anahtar listesi başlangıçta boştur.
    for i in range(len(inputs)):
        # inputs[i], A'ya eşitse, key listesine T eklenir.
        if inputs[i] == "A":
            key.append("T")
        # inputs[i], S'ye eşitse, key listesine G eklenir.
        elif inputs[i] == "S":
            key.append("G")
        # inputs[i], T'ye eşitse, key listesine A eklenir.
        elif inputs[i] == "T":
            key.append("A")
        # inputs[i], G'ye eşitse, key listesine S eklenir.
        elif inputs[i] == "G":
            key.append("S")
    # remaining_inputs listesi, A, S, T veya G içermeyen elemanları içerir.        
    remaining_inputs = [l for l in inputs if l != "A" and l != "S" and l != "T" and l!= "G"]
    # remaining_path, remaining_inputs listesinin karakterlerinin ASCII değerlerini içeren bir liste olarak oluşturulur.
    remaining_path = [ord(l) for l in remaining_inputs]
    # zhu_takaoka() fonksiyonu çağırılır.
    remaining_key = zhu_takaoka(remaining_path)
    for idx in remaining_key:
        key.append(remaining_inputs[idx])

    return key


if __name__ == '__main__':
    dna = str(input("dna dizisi giriniz.\n"))#büyük harfler ile
    key = zhu_takaoka_for_inputs(dna)
    print(key) 
