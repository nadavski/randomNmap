# randomNmap
a basic python script to randomize Nmap scan ports and ip's

# Requirements
python3

# How does it works?
this script is a really simple python script that takes an ip list and preform nmap scan on them.
the fun part here is that it randomize the order of the scan.
instead of testing all ports on one host then moving to another, it's shuffle the ports and ip list to create a random order.
the result may help you avoid detection, and also ease the "potenital damage" of bombing old hosts with tons of ports scans.

# How to install
1. git clone the project
```
git clone https://github.com/r03i98/randomNmap.git
cd randomNmap
```
3. install the requirements
```
pip3 install requirements.txt
```



# Usage
1.to use this script load the ip_list.txt file with all the ip's you found on your target (only ip's, no domains for now..)
2. if you want to scan only 1000 most common ports run the script with:
```
python3 main.py
```
or if you want to scan all ports (0-65535) run it with:
```
python3 main.py --heavy
```
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #35;'>Update version- 2025-01-12 11:48:29</td><td>2025-01-12 11:48:29</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #34;'>Update version- 2025-01-23 16:11:02</td><td>2025-01-23 16:11:02</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #35;'>Update version- 2025-01-23 16:19:26</td><td>2025-01-23 16:19:26</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #32;'>Update version- 2025-02-10 16:55:33</td><td>2025-02-10 16:55:33</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #32;'>Update version- 2025-02-10 16:56:17</td><td>2025-02-10 16:56:17</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #33;'>Update version- 2025-02-11 02:15:54</td><td>2025-02-11 02:15:54</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #36;'>Update version- 2025-02-19 16:43:31</td><td>2025-02-19 16:43:31</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #35;'>Update version- 2025-02-20 17:39:15</td><td>2025-02-20 17:39:15</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #32;'>Update version- 2025-02-20 19:52:16</td><td>2025-02-20 19:52:16</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #36;'>Update version- 2025-02-20 19:59:18</td><td>2025-02-20 19:59:18</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #31;'>Update version- 2025-02-20 20:00:14</td><td>2025-02-20 20:00:14</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #33;'>Update version- 2025-02-20 20:02:32</td><td>2025-02-20 20:02:32</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #33;'>Update version- 2025-02-21 10:04:54</td><td>2025-02-21 10:04:54</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #33;'>Update version- 2025-02-23 13:28:54</td><td>2025-02-23 13:28:54</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #33;'>Update version- 2025-02-24 15:01:05</td><td>2025-02-24 15:01:05</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #32;'>Update version- 2025-02-24 15:02:49</td><td>2025-02-24 15:02:49</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #35;'>Update version - 2025-02-24 20:28:15</td><td>2025-02-24 20:28:15</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #35;'>Update version- 2025-02-25 16:26:14</td><td>2025-02-25 16:26:14</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #35;'>Update version- 2025-03-04 16:16:49</td><td>2025-03-04 16:16:49</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #34;'>Update version- 2025-03-04 19:04:58</td><td>2025-03-04 19:04:58</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #32;'>Update version- 2025-03-05 15:28:45</td><td>2025-03-05 15:28:45</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #34;'>Update version- 2025-03-07 08:34:43</td><td>2025-03-07 08:34:43</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #34;'>Update version- 2025-03-12 13:25:33</td><td>2025-03-12 13:25:33</td></tr>
</table>
<h3>Changes</h3>
<table border="1">
<tr><th>Change Description</th><th>Date</th></tr>
<tr><td style='color: #32;'>Update version- 2025-03-26 10:29:45</td><td>2025-03-26 10:29:45</td></tr>
</table>
