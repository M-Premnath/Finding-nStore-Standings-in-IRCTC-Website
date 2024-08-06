# Finding-nStore-Standings-in-IRCTC-Website
Developed a Python solution to locate nStore positions at each station on the IRCTC e-catering website, extracting and processing the data, and saving the results as a CSV file for reporting and analysis.
<h1>Script Summary</h1>
<p>This script fetches and processes station outlet data from the IRCTC e-catering API and saves it to a CSV file. The script performs the following tasks:</p>

<ol>
    <li>
        <strong>Import Required Libraries:</strong> The script uses the <code>csv</code>, <code>json</code>, <code>os</code>, and <code>requests</code> libraries.
    </li>
    <li>
        <strong>Station Data:</strong> The script includes a JSON string with station code and name details for various stations.
    </li>
    <li>
        <strong>URL Template:</strong> A URL template is provided, which will be used to fetch outlet data for each station using its station code.
    </li>
    <li>
        <strong>Parse Station Data:</strong> The station data JSON string is parsed into a Python dictionary.
    </li>
    <li>
        <strong>Clear Existing CSV File:</strong> If the CSV file <code>nStore position data.csv</code> exists, it is deleted to start fresh.
    </li>
    <li>
        <strong>Open CSV File:</strong> A CSV file is opened in append mode. If the file is empty, a header row is written.
    </li>
    <li>
        <strong>Fetch and Process Data for Each Station:</strong>
        <ol>
            <li>For each station, the station code and name are extracted.</li>
            <li>A URL is constructed using the station code.</li>
            <li>A request is sent to the API to fetch outlet data.</li>
            <li>If the request is successful, the JSON response is parsed to extract the total number of outlets and the position of "nStore Technologies Pvt Ltd" vendor (if available).</li>
            <li>The data is then written to the CSV file.</li>
            <li>If the request fails, an error message is written to the CSV file.</li>
        </ol>
    </li>
    <li>
        <strong>Increment Serial Number:</strong> A serial number is incremented for each station to maintain a sequential order in the CSV file.
    </li>
</ol>
<h1>This is the Sample output of the program:</h1>
<table>
    <thead>
        <tr>
            <th>S.No</th>
            <th>Station Name</th>
            <th>Station Code</th>
            <th>Total Outlets</th>
            <th>nStore Index</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Agra Cantonment</td>
            <td>AGC</td>
            <td>29</td>
            <td>16</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Jolarpettai</td>
            <td>JTJ</td>
            <td>8</td>
            <td>8</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Kanpur Central</td>
            <td>CNB</td>
            <td>46</td>
            <td>17</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Tuticorin</td>
            <td>TN</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Chennai Central</td>
            <td>MAS</td>
            <td>12</td>
            <td>11</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Erode JN</td>
            <td>ED</td>
            <td>16</td>
            <td>7</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Thanjavur JN</td>
            <td>TJ</td>
            <td>4</td>
            <td>4</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Coimbatore</td>
            <td>CBE</td>
            <td>14</td>
            <td>13</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Tirupur</td>
            <td>TUP</td>
            <td>15</td>
            <td>13</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Tirupati</td>
            <td>TPTY</td>
            <td>14</td>
            <td>14</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Tiruchchirappalli JN</td>
            <td>TPJ</td>
            <td>13</td>
            <td>12</td>
        </tr>
    </tbody>
</table>
