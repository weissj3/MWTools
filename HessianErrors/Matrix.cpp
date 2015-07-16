matrix::matrix()
{
    m  = 0;
    n = 0;
    initialized = false;
}

matrix::matrix(const matrix & mat)
{
    m = mat.m;
    n = mat.n;
    values = new double*[m];     
    
    for(int i = 0; i < m; i++)
    {
        values[i] = new double[n];
    }

    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            values[i][j] = mat.values[i][j];
        }
    }

    initialized = true;

}

matrix::~matrix()
{
    for(int i = 0; i < m; i++)
    {
        values[i] = delete [] double;
    }
    delete [] values;
}

matrix::matrix(unsigned int sizem, unsigned int sizen)
{
    m = sizem;
    n = sizen;
    values = new double*[m];     
    
    for(int i = 0; i < m; i++)
    {
        values[i] = new double[n];
    }
    initialized = true;
}

void matrix::setM(unsigned int y, unsigned int x, double value)
{
    if(initialized && y < m && x < n)
    {
        values[y][x] = value;
    }
    else
    {
        throw string("Inappropriate matrix access");
    }
}

double matrix::getM(unsigned int y, unsigned int x)
{
    if(initialized && y < m && x < n)
    {
        return values[y][x];
    }
    else
    {
        throw string("Inappropriate matrix access");
        return 0;
    }
}

void matrix::scale(double s)
{
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            values[i][j] *= s;
        }
    }
}


