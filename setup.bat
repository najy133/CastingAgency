@echo off

rem Set the environment variables for the Flask app

set DATABASE_URL=postgresql://postgres:Itunes132@localhost:5432/casting_agency
set AUTH0_DOMAIN=dev-ocwus3henxkqs0v2.us.auth0.com
set ALGORITHMS=RS256
set API_AUDIENCE=http://localhost:5000
set TEST_DATABASE_URL=postgresql://postgres:Itunes132@localhost:5432/casting_agency_test
set TEST_CASTING_ASSISTANT_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9jRW9hbVlJbHZ2S2tyTy1RVzZxSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1vY3d1czNoZW54a3FzMHYyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGMzZTRjNjdhYzVkYjAwYzY5NmQ1YWQiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2OTEzMzM4MTUsImV4cCI6MTY5MTQyMDIxNSwiYXpwIjoidzJuekZzZXhFblhaTm9IamVBWE9ncm43N3JIc0xoTHEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.TBWnGQOQFHEKdIOpuSDfcd3oB8QuwtZqQLq3bEvpgDkPm93rUoUyCa9t_fqmrona9pQJDn1BOzMjN1lVFGo46opS2czB4FTY0MNZZBuew3279J42FlRqN6ka2FspTFlcHL9T_Az-hCQXn98EurAaKmowzO6IlR3B7aiqNaSW9Y1y9yl7rWdXoYWmirJfA-aj58Q_65YkBxfneeULZTcBvXmpduMFAjMZSmDF0OWpJ3CuVtLphcviUr6XuoVIYcPaWyFRJcpxAQDcM5-7uNAC1KcB3jNfAyjAcDyb9TTuTU40Aeq9PvGDIgLuWgH-e5ybFKCGR1JqKEYuMRmTN-aPBw
set TEST_CASTING_DIRECTOR_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9jRW9hbVlJbHZ2S2tyTy1RVzZxSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1vY3d1czNoZW54a3FzMHYyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGMzZTUxZjdhYzVkYjAwYzY5NmQ1YzIiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2OTEzMzM5MjcsImV4cCI6MTY5MTQyMDMyNywiYXpwIjoidzJuekZzZXhFblhaTm9IamVBWE9ncm43N3JIc0xoTHEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.I1nq8GssuIX9hNR1o4hW62mRdRDMpUjc_3Z8Lo3ZIR0Z1lBmXIj5y9iKGTOKtSGiqR-IUsfNSGxu8idvAvMtlTg6KII2_qGAgUMa2rzQ9Lg-9cztVc2flFIsDgdUOMbUIHAit3JAQvfr-Vxg6gkiktvApJ5_XRDFvgcNPEOUdiqmm5JhV5aIjkXpTms_iOyhLFOYHiafUWZ0fLN_qs1ic-oM2MgWmwh3-3ez_b9RUvAWQ-jwYCkiKNYEmlsPG94LiJF9BhLo-kpLpkio2DEUwC82JbMOC6UWJXzg0rLYq75JV3KhWk9SCewgT_0nvjY3B4BF29qfkUKPOAqONimPFg

