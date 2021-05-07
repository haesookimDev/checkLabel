import pandas as pd

df = pd.read_csv("labeledComment0.csv")
df_result = pd.DataFrame(columns=['comment', 'label'])
df_rest = pd.DataFrame(columns=['comment', 'label'])

df['label'] = df['label'].astype('int16')

try:
    for comment, label in zip(df['comment'], df['label']):
        print(df[df['comment'] == comment])
        index = df[df['comment'] == comment].index.tolist()[0]
        while True:
            print("[y/n]")
            yesNo = input()
            if yesNo == 'y':
                df_result = df_result.append(
                    {'comment': comment, 'label': label},
                    ignore_index=True)
                break
            elif yesNo == 'n':
                if label == 1:
                    label = 0
                    df_result = df_result.append(
                        {'comment': comment, 'label': label},
                        ignore_index=True)
                    break
                else:
                    label = 1
                    df_result = df_result.append(
                        {'comment': comment, 'label': label},
                        ignore_index=True)
                    break
            else:
                print("다시입력\n")
                continue
    df_result['label'].astype('int16')
    df_result.to_csv("labelCommentCheck0.csv", index=False)

except KeyboardInterrupt:
    df_result['label'].astype('int16')
    df_result.to_csv("labelCommentCheck0.csv", index=False)
    df[index:].to_csv("labelCommentRest0.csv", index=False)
