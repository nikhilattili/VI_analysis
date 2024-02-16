import instaloader
import csv

# Initialize Instaloader
L = instaloader.Instaloader()

# (Optional) Log in to Instagram
username = "####"
password = "####"
L.login(username, password)  # Logging in is optional but recommended

# Define the lists of target accounts, post shortcodes, and post names
target_accounts = ['lilmiquela', 'lilmiquela', 'rocky_barnes', 'rocky_barnes']
post_shortcodes = ['Cxa38WVxTT_', 'C1ihKALtwAF','C1H7nnJOyy7', 'C0e8-z0PsKq']
post_names = ['eyewear', 'bmw', 'calvin', 'amazon']

# Iterate over each target account and its corresponding post shortcode and name
for target_account, post_shortcode, post_name in zip(target_accounts, post_shortcodes, post_names):
    # Load the target post
    post = instaloader.Post.from_shortcode(L.context, post_shortcode)

    # Open a CSV file in write mode
    with open(f'{target_account}_{post_name}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(['Username', 'Comment'])
        
        # Iterate over comments and write them to the CSV file
        for comment in post.get_comments():
            writer.writerow([comment.owner.username, comment.text])

    print(f"Comments saved to {target_account}_{post_name}.csv")
