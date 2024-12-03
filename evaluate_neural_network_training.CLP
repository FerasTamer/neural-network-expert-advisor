(deftemplate performance
   (slot accuracy)
   (slot loss)
   (slot training-accuracy)
   (slot validation-accuracy)
   (slot epochs)
   (slot learning-rate)
   (slot batch-size)
   (slot model-complexity))

(defrule low-accuracy
  (logical(performance (accuracy ?acc&:(< ?acc 0.8))))
  =>
  (assert (advice "Increase the number of epochs or adjust the learning rate.")))

(defrule high-loss
  (logical(performance (loss ?loss&:(> ?loss 0.5))))
  =>
  (assert (advice "Decrease the learning rate or add dropout layers.")))

(defrule overfitting
(logical(performance (training-accuracy ?train-acc)
               (validation-accuracy ?val-acc&:(< ?val-acc ?train-acc))))
  =>
  (assert (advice "Implement regularization techniques like L2 regularization or dropout.")))

(defrule underfitting
  (logical(performance (training-accuracy ?train-acc&:(< ?train-acc 0.8))))
  =>
  (assert (advice "Increase model complexity by adding more layers or neurons.")))

(defrule high-epoch
  (logical(performance (epochs ?epochs&:(> ?epochs 50))))
  =>
  (assert (advice "Check for overfitting; consider early stopping.")))

(defrule high-learning-rate
  (logical(performance (learning-rate ?lr&:(> ?lr 0.1))))
  =>
  (assert (advice "Decrease the learning rate.")))

(defrule low-learning-rate
  (logical(performance (learning-rate ?lr&:(< ?lr 0.0001))))
  =>
  (assert (advice "Increase the learning rate.")))

(defrule small-batch-size
  (logical(performance (batch-size ?bs&:(< ?bs 32))))
  =>
  (assert (advice "Increase the batch size.")))

(defrule large-batch-size
  (logical(performance (batch-size ?bs&:(> ?bs 512))))
  =>
  (assert (advice "Decrease the batch size.")))

(defrule low-complexity
  (logical(performance (model-complexity ?mc&:(< ?mc 3))))
  =>
  (assert (advice "Increase model complexity by adding more layers or neurons.")))

(defrule high-complexity
  (logical(performance (model-complexity ?mc&:(> ?mc 20))))
  =>
  (assert (advice "Decrease model complexity to avoid overfitting.")))
