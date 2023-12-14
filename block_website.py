import os
import windows_admin

# Define the path to the hosts file and the redirect IP
hosts_path = "C:/Windows/System32/drivers/etc/hosts" if os.name == 'nt' else "/etc/hosts"
redirect_ip = "127.0.0.1"

# List of websites to block
websites_to_block = [
    "www.youtube.com",
    "www.facebook.com"
]

# Function to block websites
def block_websites(websites_to_block):
    with open(hosts_path, 'r+') as hosts_file:
        content = hosts_file.read()
        for website in websites_to_block:
            if website not in content:
                hosts_file.write(redirect_ip + " " + website + "\n")

# Function to unblock websites
def unblock_websites(websites_to_block):
    with open(hosts_path, 'r+') as hosts_file:
        lines = hosts_file.readlines()
        hosts_file.seek(0)
        for line in lines:
            if not any(website in line for website in websites_to_block):
                hosts_file.write(line)
        hosts_file.truncate()


if __name__ == "__main__":
    # Call the block function to block the websites
    windows_admin.running_with_admin(block_websites, websites_to_block)

    # Uncomment the line below to unblock the websites
    # windows_admin.running_with_admin(unblock_websites, websites_to_block)

