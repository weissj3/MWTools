
 wedge = 20
 
 background = { 
   q  = 0.5, 
   r0 = 12.0
 } 
 
 streams = { 
   { 
      epsilon = -1.5,
      mu      = 190.0,
      r       = 33.9,
      theta   = 1.85,
      phi     = 3.05,
      sigma   = 4.5
   },

   { 
      epsilon = .95,
      mu      = 210.0,
      r       = 35.53,
      theta   = 1.5,
      phi     = 3.18,
      sigma   = 10.0
   },

   { 
      epsilon = -.93,
      mu      = 180.0,
      r       = 14.56,
      theta   = 1.97,
      phi     = -0.4,
      sigma   = 4.16
   }
}

area = {
   {
      r_min = 16,
      r_max = 22.5,
      r_steps = 70,

      mu_min = 133,
      mu_max = 249,
      mu_steps = 80,

      nu_min = -1.25,
      nu_max = 1.25,
      nu_steps = 32
   }
}
