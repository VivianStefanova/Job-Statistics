import unittest
import src.SQL_utils as sql
class get_insert_values_tests(unittest.TestCase):
    dict_API = {'description': 'Position Summary: More than 15 years in IT infrastructure of which 5 plus years directly working with customer in onsite and should have worked 2/3 years with current organization. Excellent customer engagement and Negotiation and CRM Skill. Bachelor’s degree or equivalent certifications. Minimum of 4 years hands on work experience in any area of Infrastructure Operations, Network Operations, Service Desk. Experience in Project/Program Management in relevant areas like Service Desk, Infrastruct…', 'redirect_url': 'https://www.adzuna.co.uk/jobs/details/5039776326?utm_medium=api&utm_source=840352a3', 'location': {'display_name': 'London, UK', '__CLASS__': 'Adzuna::API::Response::Location', 'area': ['UK', 'London']}, 'contract_time': 'full_time', 'category': {'label': 'IT Jobs', '__CLASS__': 'Adzuna::API::Response::Category', 'tag': 'it-jobs'}, 'adref': 'eyJhbGciOiJIUzI1NiJ9.eyJzIjoiV044VEF0RG03eEduVGZYZ0RjbHF0USIsImkiOiI1MDM5Nzc2MzI2In0.b0RNVsu5Kdo_CCpmzcNsGYV7wdw-NUvcVkMRo5hYCYw', 'created': '2025-02-06T11:44:05Z', 'salary_min': 85000, 'salary_max': 85000, '__CLASS__': 'Adzuna::API::Response::Job', 'id': '5039776326', 'company': {'display_name': 'Code Convergence', '__CLASS__': 'Adzuna::API::Response::Company'}, 'longitude': -0.139134, 'salary_is_predicted': '0', 'title': 'Service delivery Manager ( experience of offshore model )', 'contract_type': 'permanent', 'latitude': 51.503378}
    dict_MITM = {'id': '30d3b5d654ffeb1633abc56431ab507e', 'title': 'REMOTE Structural Engineer', 'jobLocation': {'displayName': 'US'}, 'postedDate': '2025-02-08T13:19:03Z', 
                'detailsPageUrl': 'https://www.dice.com/job-detail/325ad40a-d81d-427e-92dc-878becad82b2', 'companyPageUrl': 'https://www.dice.com/company/91113390', 'companyLogoUrl': 'https://d3qscgr6xsioh.cloudfront.net/RVkPsbuFScmLFloqItyr_transformed.png?format=webp', 'companyLogoUrlOptimized': 'https://d3qscgr6xsioh.cloudfront.net/RVkPsbuFScmLFloqItyr_transformed.png?format=webp', 'salary': 'USD 120,000.00 - 140,000.00 per year', 'clientBrandId': '91113390', 'companyName': 'Jobot', 'employmentType': 'Full-time', 'summary': 'Work For a Company Who Believes in an Amazing Employee Culture and Career Growth!!  This Jobot Job is hosted by: Kristin Ursua Are you a fit? Easy Apply now by clicking the "Apply Now" button and sending us your resume. Salary: $120,000 - $140,000 per year  A bit about us:  We are a 70+ years strong leader in the Property Insurance Intelligence Industry. Our purpose is to provide actionable intelligence for tough questions about property and property contents. From our testing labs to fire inves', 'jobId': '30d3b5d654ffeb1633abc56431ab507e', 'score': 253.47673, 'easyApply': False, 
                'willingToSponsor': False, 'employerType': 'Recruiter', 'workFromHomeAvailability': 'FALSE', 'isRemote': True, 'modifiedDate': '2025-02-09T01:18:07Z', 'guid': '325ad40a-d81d-427e-92dc-878becad82b2', 'workplaceTypes': ['Remote']}
    def test_clean_date(self):
        self.assertEqual(sql.clean_date("2025-02-06T11:44:05Z"), "2025-02-06")
        self.assertEqual(sql.clean_date("2025-02-08T13:19:03Z"), "2025-02-08")
    def test_clean_contract_time(self):
        self.assertEqual(sql.clean_contract_time("full_time"), "full_time")
        self.assertEqual(sql.clean_contract_time("part_time"), "part_time")
        self.assertEqual(sql.clean_contract_time("contract"), "contract")
        self.assertEqual(sql.clean_contract_time("third_party"), "third_party")
        self.assertEqual(sql.clean_contract_time("unknown"), "unknown")
        self.assertEqual(sql.clean_contract_time("Full Time"), "full_time")
        self.assertEqual(sql.clean_contract_time("Part_time"), "part_time")
        self.assertEqual(sql.clean_contract_time("Contract"), "contract")
    def test_get_insert_values_MITM_scraper(self):
        self.assertEqual(sql.get_insert_values_MITM_scraper(self.dict_MITM), 
                         ('REMOTE Structural Engineer', 'Jobot', '2025-02-08', 120000, 140000, 'US', 'full_time', True))
       
        dict_m_1 = {'id': '30d3b5d654ffeb1633abc56431ab507e', 'title': 'REMOTE Structural Engineer', 
                'detailsPageUrl': 'https://www.dice.com/job-detail/325ad40a-d81d-427e-92dc-878becad82b2', 'companyPageUrl': 'https://www.dice.com/company/91113390', 'companyLogoUrl': 'https://d3qscgr6xsioh.cloudfront.net/RVkPsbuFScmLFloqItyr_transformed.png?format=webp', 'companyLogoUrlOptimized': 'https://d3qscgr6xsioh.cloudfront.net/RVkPsbuFScmLFloqItyr_transformed.png?format=webp',  'clientBrandId': '91113390', 'companyName': 'Jobot',  'summary': '   A bit about us:  We are a 70+ years strong leader in the Property Insurance Intelligence Industry. Our purpose is to provide actionable intelligence for tough questions about property and property contents. From our testing labs to fire inves', 'jobId': '30d3b5d654ffeb1633abc56431ab507e', 'score': 253.47673, 'easyApply': False, 
                'willingToSponsor': False, 'employerType': 'Recruiter', 'workFromHomeAvailability': 'FALSE', 'isRemote': True, 'modifiedDate': '2025-02-09T01:18:07Z', 'guid': '325ad40a-d81d-427e-92dc-878becad82b2', 'workplaceTypes': ['Remote']}
        self.assertEqual(sql.get_insert_values_MITM_scraper(dict_m_1), 
                         ('REMOTE Structural Engineer', 'Jobot', '0000-00-00',-2,-2, 'unknown', 'unknown', True))
    def test_get_insert_values_API_scraper(self):
        self.assertEqual(sql.get_insert_values_API_scraper(self.dict_API), 
                         ('Service delivery Manager ( experience of offshore model )', 'Code Convergence', '2025-02-06', 85000, 85000, 'UK', 'full_time', 'unknown')) 
           
        dict_a_1 = {'description': 'Position Summary: anagement in relevant areas like Service Desk, Infrastruct…', 'redirect_url': 'https://www.adzuna.co.uk/jobs/details/5039776326?utm_medium=api&utm_source=840352a3', 'category': {'label': 'IT Jobs', '__CLASS__': 'Adzuna::API::Response::Category', 'tag': 'it-jobs'}, 'adref': 'eyJhbGciOiJIUzI1NiJ9.eyJzIjoiV044VEF0RG03eEduVGZYZ0RjbHF0USIsImkiOiI1MDM5Nzc2MzI2In0.b0RNVsu5Kdo_CCpmzcNsGYV7wdw-NUvcVkMRo5hYCYw', 'created': '2025-02-06T11:44:05Z',  '__CLASS__': 'Adzuna::API::Response::Job', 'id': '5039776326', 'longitude': -0.139134, 'salary_is_predicted': '0', 'title': 'Service delivery Manager ( experience of offshore model )', 'contract_type': 'permanent', 'latitude': 51.503378}
        self.assertEqual(sql.get_insert_values_API_scraper(dict_a_1), 
                         ('Service delivery Manager ( experience of offshore model )', 'unknown', '2025-02-06', -2, -2, 'unknown', 'unknown', 'unknown'))
if __name__ == '__main__':
    unittest.main() 