def update_weight(m, b, X, Y, learning_rate):
    m_deriv = 0
    b_deriv = 0
    N =  len(X)
    for i in range(N):
        # caculate partial derivatives
        # for m: -2x(y - (mx + b))
        m_deriv += -2 * X[i] * (Y[i] - (m * X[i] + b))

        # for b: -2(y- (mx + b))
        b_deriv += -2 * (Y[i] - (m * X[i] + b))

    m -= (m_deriv / float(N)) * learning_rate
    b -= (b_deriv / float(N)) * learning_rate
    return m, b

