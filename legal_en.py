# English legal pages. Rendered by build.py.
#
# These are DRAFTS and must be reviewed by a lawyer before publication.
# The Turkish texts are the reference versions.

RECIPIENTS_TABLE = """
<div class="table-scroll">
<table>
  <thead>
    <tr><th>Recipient</th><th>Country</th><th>Data</th><th>Purpose</th></tr>
  </thead>
  <tbody>
    <tr><td>Supabase Inc.</td><td>{{SUPABASE_REGION_EN}}</td><td>Account, profile, book entries, reading list, goals, recommendation history, profile photo, session and access logs</td><td>Database, authentication, file storage and server functions</td></tr>
    <tr><td>Anthropic PBC</td><td>USA</td><td>Title, author and country of the books you have read; previously recommended works; the request you type to the assistant. Your name, email address and user ID are not sent.</td><td>Generating AI book and movie recommendations</td></tr>
    <tr><td>Google LLC (Google Books)</td><td>USA</td><td>Your book search query or ISBN (relayed through our server); your IP address when a cover image loads</td><td>Book details and cover images</td></tr>
    <tr><td>Internet Archive (Open Library)</td><td>USA</td><td>Your book search query or ISBN (relayed through our server); your IP address when a cover image loads</td><td>Book details and cover images</td></tr>
    <tr><td>OpenStreetMap Foundation (Nominatim)</td><td>United Kingdom</td><td>The city and country name you enter on a book entry (relayed through our server)</td><td>Placing the city on the map</td></tr>
    <tr><td>OMDb API and the servers hosting poster images</td><td>USA</td><td>Title and year of a recommended movie (relayed through our server); your IP address when a poster image loads</td><td>Movie poster image</td></tr>
    <tr><td>GitHub, Inc. (GitHub Pages)</td><td>USA</td><td>Your IP address when you open the legal pages from within the App</td><td>Publishing the legal documents and this website</td></tr>
  </tbody>
</table>
</div>
"""

CONTACT = """
<div class="box">
  <p><strong>Data controller:</strong> {{CONTROLLER}}<br>
  {{ADDRESS_LINE}}
  <strong>Email:</strong> {{EMAIL}}</p>
</div>
"""

PAGES = {}

PAGES["privacy_policy"] = {
    "title": "Privacy Policy",
    "h1": "Privacy Policy",
    "description": "How BookAtlas collects, uses, shares and protects your personal data.",
    "tr": "tr/aydinlatma-metni-uyeler.html",
    "body": """
<p>This Privacy Policy explains how the BookAtlas mobile app (“BookAtlas”, the “App”) handles your personal data. BookAtlas is operated by {{CONTROLLER}}, who is the data controller.</p>
""" + CONTACT + """
<div class="box">
  <p><strong>In short:</strong> we store what you put into the App so we can show it back to you as a map, a list and statistics. We do not show ads, we do not use third-party analytics, and we do not sell your data. You can export your books and delete your account at any time.</p>
</div>

<h2>1. Data we process</h2>
<ul>
  <li><strong>Identity:</strong> full name, username, date of birth.</li>
  <li><strong>Contact:</strong> email address.</li>
  <li><strong>Image:</strong> your profile photo, if you upload one.</li>
  <li><strong>Your content and activity:</strong> the books you log (title, author, ISBN, country, city, reader name, finish date and your notes), your reading list, reading goals, reading statistics, the short bio on your profile, a record of map cards you share, the requests you type to the AI assistant, and the history of book and movie recommendations you receive.</li>
  <li><strong>Subscription:</strong> Premium status, plan, purchased product, store, start and end dates. We never receive your payment card details; payments are taken by the App Store or Google Play.</li>
  <li><strong>Legal records:</strong> when you accepted the Terms of Use, this Privacy Policy and the Explicit Consent Statement, which version you accepted, and your confirmation that you are at least 13.</li>
  <li><strong>Security:</strong> IP address, session and access logs, and daily usage counts for the AI and search features.</li>
  <li><strong>Preferences:</strong> your language preference and app settings, which are stored locally on your device together with your session.</li>
</ul>
<p>The App does not request location permission; you type the country and city yourself. The camera is used only to scan a book barcode or, if you choose, take a profile photo. The photo library is used only to pick a profile photo.</p>
<p>Book notes are free text. Please do not enter sensitive information about yourself (such as health, beliefs or political views) or personal data about other people.</p>

<h2>2. Why we process it</h2>
<ul>
  <li>To create and manage your account and verify your identity.</li>
  <li>To store your book entries and build your world map, reading list, goals and statistics.</li>
  <li>To search for books, look up ISBNs and show cover images.</li>
  <li>To prepare AI book and movie recommendations based on your reading history and your request.</li>
  <li>To run Premium subscriptions and free trials.</li>
  <li>To prevent abuse, apply daily usage limits and keep the service secure.</li>
  <li>To answer your requests and complaints.</li>
  <li>To fix bugs and improve the service.</li>
  <li>To comply with legal obligations.</li>
</ul>
<p>We do not use your data for advertising or sell it to third parties.</p>

<h2>3. Legal bases</h2>
<ul>
  <li><strong>Performance of a contract:</strong> your account and all core features, including AI recommendations and subscriptions.</li>
  <li><strong>Legitimate interests:</strong> preventing abuse, security, fixing bugs and improving the service.</li>
  <li><strong>Legal obligation:</strong> responding to lawful requests from authorities and meeting retention duties.</li>
  <li><strong>Consent:</strong> the transfer of your data to service providers outside Türkiye, as described in the <a href="explicit_consent.html">Explicit Consent Statement</a>.</li>
</ul>

<h2>4. Who we share it with</h2>
<p>We share personal data only with the service providers that are needed to run the App. Their servers are located outside Türkiye and, for some users, outside their own country.</p>
""" + RECIPIENTS_TABLE + """
<p>We may also disclose data to public authorities when we are legally required to do so.</p>

<h2>5. AI recommendations</h2>
<p>Book and movie recommendations are generated by an AI model and may contain mistakes. They are suggestions only and have no legal or similarly significant effect on you. To prepare a recommendation we send the titles, authors and countries of books you have read, plus any request you type; we do not send your name, email address or user ID. You can send feedback or objections about recommendations to {{EMAIL}}.</p>

<h2>6. How long we keep it</h2>
<p>We keep your data for as long as your account exists or until you ask us to delete it. Access and activity logs are kept for no more than 12 months. When you delete your account, your account details, book entries, reading list, goals, recommendation history and profile photo are deleted. Records we are legally required to keep, or that are needed to establish or defend a legal claim, are kept for the relevant statutory period and then deleted or anonymised. See <a href="account_deletion.html">Account Deletion</a>.</p>

<h2>7. Security</h2>
<ul>
  <li>Data is transmitted over TLS/SSL encryption.</li>
  <li>Access to records is controlled with Supabase Row Level Security (RLS).</li>
  <li>Passwords are stored as hashes.</li>
  <li>Keys for third-party services are held on the server, not in the App.</li>
  <li>Security updates are applied regularly.</li>
</ul>

<h2>8. Children</h2>
<p>BookAtlas is not directed at children under 13, and you must be at least 13 to create an account. If you are under 18, you may use the App only with the consent of a parent or guardian. If you believe a child under 13 has created an account, contact us and we will delete it.</p>

<h2>9. Your rights</h2>
<p>Under the Turkish Personal Data Protection Law No. 6698 you have the right to learn whether your data is processed, request information about it, learn the purpose of processing, know the third parties it is transferred to, request correction or deletion, object to results arising from solely automated analysis, and claim compensation for unlawful processing.</p>
<p>If you are in the European Economic Area or the United Kingdom, you also have the right to access, rectify, erase and port your data, to restrict or object to processing, to withdraw consent at any time, and to lodge a complaint with your local data protection authority.</p>
<p>To exercise your rights, write to {{WRITTEN_ROUTE}}{{EMAIL}} from the email address registered to your account. We respond within 30 days at the latest.</p>

<h2>10. Changes</h2>
<p>We may update this policy when our processing or the law changes. The current version is always published on this page, and we announce significant changes in the App.</p>
""",
}

PAGES["terms_of_use"] = {
    "title": "Terms of Use",
    "h1": "Terms of Use",
    "description": "The terms that govern your use of the BookAtlas mobile app.",
    "tr": "tr/kullanici-sozlesmesi.html",
    "body": """
<p>By creating an account or using the BookAtlas mobile app, you agree to these Terms of Use (the “Terms”). If you do not agree, please do not use the App.</p>

<h2>1. Parties</h2>
<p>These Terms are an agreement between {{CONTROLLER}}, the operator of the BookAtlas mobile app (“BookAtlas”, the “App”), and you, an individual using the App for personal, non-commercial purposes (the “User”).</p>

<h2>2. The service</h2>
<p>BookAtlas lets you log the books you read by country and city, see them on a world map, keep a reading list and reading goals, follow your reading statistics, and receive AI book and movie recommendations.</p>

<h2>3. Your account</h2>
<ul>
  <li>You need a valid email address and a password to create an account.</li>
  <li>You must be at least 13 years old. If you are under 18, you may use the App only with the consent of a parent or guardian.</li>
  <li>The information you provide must be accurate and your own.</li>
  <li>You are responsible for keeping your password confidential. Tell us promptly if you believe your account has been used without your permission.</li>
  <li>Each user may create only one account, and the free trial can be used once per user.</li>
</ul>

<h2>4. Acceptable use</h2>
<p>You agree:</p>
<ul>
  <li>to use the App only for personal and lawful purposes;</li>
  <li>not to use a username, profile photo or content that is unlawful, abusive or threatening, or that infringes anyone’s personal or intellectual property rights;</li>
  <li>not to record or share other people’s personal data without permission;</li>
  <li>not to compromise the security of the App, disrupt it, or interfere with other users;</li>
  <li>not to access the App with automated tools, try to bypass daily usage limits, reverse engineer or copy the App;</li>
  <li>not to use the App for commercial or advertising purposes.</li>
</ul>

<h2>5. Your content</h2>
<p>The book entries, notes and other content you add belong to you. You allow us to store and process that content solely to provide the service to you. You can export your entries from the App and remove them by deleting your account.</p>
<p>Images created with sharing features, such as the map card, are shared by you, where you choose; you are responsible for what you share.</p>

<h2>6. AI recommendations</h2>
<ul>
  <li>Book and movie recommendations are generated by an AI model, are for information only and may contain mistakes. We do not guarantee the accuracy of a recommended title, author or description.</li>
  <li>Recommendation features have daily usage limits, which differ between free and Premium accounts and are shown in the App.</li>
  <li>We may change these limits going forward to keep the service sustainable. For Premium members, less favourable changes apply from the end of the current subscription period.</li>
</ul>

<h2>7. Premium, free trial and payment</h2>
<ul>
  <li>The core features of the App are free. Premium unlocks the additional features and higher usage limits described in the App.</li>
  <li>The price and period are shown by the App Store or Google Play at the time of purchase. Payments are taken by those stores; BookAtlas does not have access to your payment card details.</li>
  <li>Subscriptions renew automatically for the same period unless cancelled at least 24 hours before the end of the current period. You can cancel at any time in your store account settings; access continues until the end of the period you have paid for.</li>
  <li>Refund requests are handled by the store where you made the purchase, under its refund rules.</li>
  <li>Free trials and campaigns are subject to the conditions announced in the App. A free trial is available once per user; when it ends, access ends automatically and no fee is charged. We may change campaign conditions going forward or end a campaign.</li>
  <li>Deleting your account does not cancel a store subscription. You must cancel it separately in your store account settings.</li>
</ul>
<p>Nothing in these Terms limits the rights you have under consumer protection law.</p>

<h2>8. Third-party content and services</h2>
<p>Book details and cover images come from third-party sources such as Google Books and Open Library; movie posters come from OMDb. We do not guarantee that this information is complete or up to date. Third-party websites opened from the App are subject to their own terms.</p>

<h2>9. Intellectual property</h2>
<p>The software, design, name, logo and all other elements of the App belong to BookAtlas and may not be copied, reproduced, distributed or used to create derivative works without written permission. Rights in book titles, cover images and movie posters belong to their respective owners.</p>

<h2>10. Changes, suspension and termination</h2>
<ul>
  <li>We may add, change or remove features, and may temporarily suspend the service for maintenance, updates or security reasons.</li>
  <li>We may suspend or terminate an account that is used in breach of these Terms or the law, or that appears to be used by an unauthorised person.</li>
</ul>

<h2>11. Liability</h2>
<p>We take reasonable care to keep the App available and free of errors, but we do not promise that it will always be uninterrupted or error-free. Except in cases of intent or gross negligence, BookAtlas is not liable for losses arising from your use of the App in breach of these Terms, from outages caused by third-party service providers, or from decisions you make based on AI recommendations. This section does not limit any rights you have under mandatory law.</p>

<h2>12. Personal data</h2>
<p>Your personal data is processed as described in the <a href="privacy_policy.html">Privacy Policy</a>.</p>

<h2>13. Force majeure</h2>
<p>Neither party is liable for failing to perform its obligations because of events it could not foresee or prevent, such as natural disasters, epidemics, war, strikes, changes in law, or infrastructure and communication outages. Obligations are suspended until the event ends.</p>

<h2>14. Changes to these Terms</h2>
<p>We may update these Terms for technical reasons or to comply with the law. The current version is published on this page, and we announce significant changes that affect your rights in the App in advance. If you do not accept a change, you can end the agreement by deleting your account.</p>

<h2>15. Term and termination</h2>
<p>These Terms apply from the moment you create an account and for as long as it exists. You can end the agreement at any time by using “Delete Account” in the App or by writing to {{EMAIL}}. See <a href="account_deletion.html">Account Deletion</a>.</p>

<h2>16. Governing law and disputes</h2>
<p>These Terms are governed by the laws of the Republic of Türkiye, and {{COURT}} have jurisdiction over disputes. Your right to apply to consumer arbitration committees and consumer courts under Turkish consumer law is reserved. If you are a consumer resident in another country, you keep the protection of the mandatory consumer rules of that country.</p>

<h2>17. Language</h2>
<p>These Terms are provided in Turkish and English. If the two versions differ, the <a href="tr/kullanici-sozlesmesi.html">Turkish version</a> prevails to the extent permitted by law.</p>

<h2>18. Contact</h2>
""" + CONTACT,
}

PAGES["account_deletion"] = {
    "title": "Account Deletion",
    "h1": "Account Deletion",
    "description": "How to delete your BookAtlas account and data.",
    "tr": "tr/hesap-silme.html",
    "body": """
<p>You can permanently delete your BookAtlas account and the data linked to it in either of the following ways.</p>

<h2>Option 1: In the app</h2>
<ol>
  <li>Open BookAtlas.</li>
  <li>Go to your profile.</li>
  <li>Tap “Delete Account”.</li>
  <li>Enter your password to confirm.</li>
</ol>

<h2>Option 2: By email</h2>
<p>If you cannot access the App, send an email with the subject “BookAtlas Account Deletion Request” to {{EMAIL}} from the email address registered to your account, stating that address and your full name. Requests are processed within 7 business days after we verify your identity.</p>

<h2>What is deleted</h2>
<p>When your account is deleted, the following are removed permanently and cannot be restored:</p>
<ul>
  <li>your account and profile details (email, name, username, date of birth, profile photo);</li>
  <li>all of your book entries and your world map;</li>
  <li>your reading list and reading goals;</li>
  <li>your AI book and movie recommendation history;</li>
  <li>your statistics and sharing records;</li>
  <li>your Premium membership record.</li>
</ul>
<p>Deletion cannot be undone. Removing data completely from backup systems can take up to 30 days. Records we are legally required to keep may be retained for the relevant statutory period. You can create a new account with the same email address, but you will not have access to your old data.</p>

<div class="box">
  <p><strong>If you have an active subscription:</strong> deleting your account does not cancel your store subscription. To avoid further charges, cancel it in your App Store or Google Play account settings before deleting your account.</p>
  <p><strong>If you want to keep your records:</strong> before deleting, use the export button on the Statistics page to download your book entries as a CSV file.</p>
</div>
""",
}

PAGES["explicit_consent"] = {
    "title": "Explicit Consent Statement",
    "h1": "Explicit Consent Statement",
    "description": "Consent to the transfer of BookAtlas members' personal data to service providers outside Türkiye.",
    "tr": "tr/acik-riza-beyani.html",
    "body": """
<p>I have read the <a href="privacy_policy.html">Privacy Policy</a> and have been informed about how my personal data is processed.</p>

<div class="box">
  <p>Under Article 9 of the Turkish Personal Data Protection Law No. 6698, I consent to the transfer of my account and profile details, book entries, reading list, reading goals, recommendation history and subscription details by the data controller {{CONTROLLER}} to the service providers listed below, whose servers are located outside Türkiye, solely for the purposes described in the Privacy Policy.</p>
</div>

<h2>Service providers</h2>
""" + RECIPIENTS_TABLE + """
<h2>I understand that</h2>
<ul>
  <li>I am not obliged to give this consent, but because BookAtlas runs on service providers located outside Türkiye, an account cannot be created without it;</li>
  <li>the countries my data is transferred to may not offer a level of data protection equivalent to that in Türkiye;</li>
  <li>I can withdraw my consent at any time, without giving a reason, by writing to {{EMAIL}} or by deleting my account; withdrawal takes effect for the future and ends my membership;</li>
  <li>I can exercise my rights as described in the Privacy Policy.</li>
</ul>
<p>This statement is a translation. The <a href="tr/acik-riza-beyani.html">Turkish version</a> prevails if the two differ.</p>
""",
}

NAV = [
    ("terms_of_use", "Terms of Use"),
    ("privacy_policy", "Privacy Policy"),
    ("explicit_consent", "Explicit Consent"),
    ("account_deletion", "Account Deletion"),
]
