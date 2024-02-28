import instaloader
import csv

L = instaloader.Instaloader()

username = "####"
password = "####"
L.login(username, password) 

target_accounts = ['lilmiquela', 'lilmiquela', 'rocky_barnes', 'rocky_barnes']
post_shortcodes = ['Cxa38WVxTT_', 'C1ihKALtwAF','C1H7nnJOyy7', 'C0e8-z0PsKq']
post_names = ['eyewear', 'bmw', 'calvin', 'amazon']

for target_account, post_shortcode, post_name in zip(target_accounts, post_shortcodes, post_names):
    post = instaloader.Post.from_shortcode(L.context, post_shortcode)

    with open(f'{target_account}_{post_name}.csv', 'w', newline='', encoding='utf-8') as csvfile:

        writer = csv.writer(csvfile)
        writer.writerow(['Username', 'Comment'])
        
        for comment in post.get_comments():
            writer.writerow([comment.owner.username, comment.text])

    print(f"Comments saved to {target_account}_{post_name}.csv")
