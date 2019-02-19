import lib
import json

class ComplianceReportPull():
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.csvreader = lib.CsvReader()
        self.rl_sess = lib.RLSession(self.config.rl_user,self.config.rl_pass,self.config.rl_cust)
        self.email_send = lib.EmailHelper()

    def build(self):
        self.url = "https://api.redlock.io/report"
        self.rl_sess.authenticate_client()
        resp = self.rl_sess.client.get(self.url)
        json_resp = resp.json()
        readcsv = self.csvreader.read()
        report_count = 0
        for row in readcsv:
            for item in json_resp:
                if row["Report Name"] == item["name"]:
                    self.downloadurl = "https://api.redlock.io/report/%s/download" % item["id"]
                    #self.rl_sess.authenticate_client()
                    download_resp = self.rl_sess.client.get(self.downloadurl)
                    download_path = "downloads/" + row["Report Name"] + ".pdf"
                    open(download_path, 'wb').write(download_resp.content)
                    self.email_send.send_email(row["Email address"],"Subject Here",download_path)
                    print "Sending email to: %s for report: %s" % (row["Email address"],row["Report Name"])
                    report_count += 1
        print "Total reports found and downloaded: %s" % report_count


    def run(self):
        self.build()

def main():
    rl_report = ComplianceReportPull()
    rl_report.run()


if __name__ == "__main__":
    main()
