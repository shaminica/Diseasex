appendA
q0->q0: !_;R
q0->qH: _;A,S
deleteToOutput
q0->q1: x;R
q1->q1: !x;R
q1->q2: x;L
q2->q2: !x;_,L
q2->qH: x;_,S
Answer5_6
q0->q1: x;R
q1->q1: !x;R
q1->q2: x;L
q2->q2: !ACGT;L
q2->appendA: A;y,S
appendA->q3: A;S
q2->appendC: C;y,S
appendC->q3: C;S
q2->appendG: G;y,S
appendG->q3: G;S
q2->appendT: T;y,S
appendT->q3: T;S
q3->q3: !y;L
q3->q2: y;L
q2->deleteToOutput: x;S
deleteToOutput->appendx: x;S
appendx->qH: x;S


block: qBinIncr=binaryIncrementer.tm
block: qShiftInt=shiftInteger.tm