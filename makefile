get-leader:
	python ./simulations/simulate.py queue --query-leader-of test-quorum-queue

shutdown-leader:
	python ./simulations/simulate.py queue --shutdown-leader-of test-quorum-queue