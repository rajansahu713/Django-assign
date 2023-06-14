from .test_setup import TestSetup

class TestViews(TestSetup):
    def test_userprofile_without_data(self):
        resp = self.client.post(self.user_profile)
        self.assertEqual(resp.status_code, 400)

    def test_userprofile_with_data(self):
        
        resp = self.client.post(self.user_profile,self.data)
        self.assertEqual(resp.status_code, 201)

    def test_userprofile_with_response(self):

        resp = self.client.post(self.user_profile,self.data)
        response=resp.json()
        self.assertEqual(response["data"]["id"], 1)

    def test_userprofile_with_response_status(self):
        
        resp = self.client.post(self.user_profile,self.data)
        response=resp.json()
        self.assertEqual(response["success"], True)

    def test_userprofile_with_update(self):
        resp = self.client.post(self.user_profile,self.data)
        response=resp.json()
        id=response['data']['id']

        data_update={         
            "name": "test",
            "email":"test@12.com",
            "bio":"hello"
        }
        resp = self.client.patch(f"{self.user_profile}?id={id}",data_update)
        self.assertEqual(resp.status_code, 200)

    def test_userprofile_with_update_without_passing_query_params(self):
        data_update={         
            "name": "test",
            "email":"test@12.com",
            "bio":"hello"
        }
        resp = self.client.patch(f"{self.user_profile}?",data_update)
        self.assertEqual(resp.status_code, 400)
