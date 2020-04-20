# coding=utf-8
import collections
import pkuseg

if __name__ == '__main__':
    # 分词
    pkuseg.test('details.txt', 'seg_out.txt')
    f = open('seg_out.txt', 'r', encoding='utf-8')
    lst = str(f.read()).replace('\n', '').replace(',', '').replace('、', '').replace('：', '').replace('。', '').replace('；', '').split(' ')
    f.close()

    # 读取停用词
    f = open('cn_stopwords.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    stop_words = []
    for item in lines:
        stop_words.append(item[:-1])

    print(len(stop_words))

    counts_dict = collections.Counter(lst)
    f = open('seg_counts.txt', 'w', encoding='utf-8')
    for item in counts_dict:
        # 只写入非停用词、字数大于1个、出现次数高于30
        if (item not in stop_words) & (len(item) > 1) & (counts_dict[item] > 30):
            f.write('%s,%s\n' % (item, counts_dict[item]))

    f.close()
    print('ok')
